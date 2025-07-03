#!/usr/bin/env python3
import argparse
import bisect
import re
import subprocess
import sys
import xml.etree.ElementTree as ET


def get_changed_ranges(file_path, git_diff_range):
    """Get changed line ranges for a file"""
    try:
        cmd = f"git diff -U0 {git_diff_range} -- {file_path}"
        result = subprocess.run(cmd.split(), capture_output=True, text=True)

        ranges = []
        for line in result.stdout.split("\n"):
            if line.startswith("@@"):
                match = re.search(r"\+(\d+)(?:,(\d+))?", line)
                if match:
                    start = int(match.group(1))
                    count = int(match.group(2)) if match.group(2) else 1
                    if count > 0:
                        ranges.append((start, start + count - 1))
        return ranges
    except Exception as e:
        print(f"Error getting changed lines for {file_path}: {e}")
        return []


def is_line_in_ranges(line_num, ranges):
    """Check if line number is in any of the ranges"""
    if len(ranges) <= 5:  # Linear search for small number of ranges
        return any(start <= line_num <= end for start, end in ranges)

    # Binary search for larger number of ranges
    # Sort ranges by start position
    sorted_ranges = sorted(ranges)
    # Find insertion point
    idx = bisect.bisect_left(sorted_ranges, (line_num, line_num))

    # Check range at idx and idx-1
    for i in [idx - 1, idx]:
        if 0 <= i < len(sorted_ranges):
            start, end = sorted_ranges[i]
            if start <= line_num <= end:
                return True
    return False


def filter_cppcheck_results(xml_file, git_diff_range, output_file):
    """Filter cppcheck XML results to only include changed lines"""
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        filtered_errors = []
        file_ranges_cache = {}

        for error in root.findall(".//error"):
            error_id = error.get("id", "")
            if not error_id.startswith("misra-c2012"):
                continue

            for location in error.findall("location"):
                file_path = location.get("file")
                line_num = int(location.get("line", 0))

                if file_path and line_num > 0:
                    if file_path not in file_ranges_cache:
                        file_ranges_cache[file_path] = get_changed_ranges(
                            file_path, git_diff_range
                        )

                    ranges = file_ranges_cache[file_path]
                    if is_line_in_ranges(line_num, ranges):
                        filtered_errors.append(error)
                        break

        # Create new XML with filtered results
        new_root = ET.Element("results")
        new_root.set("version", root.get("version", "2"))

        cppcheck_elem = ET.SubElement(new_root, "cppcheck")
        cppcheck_elem.set("version", root.find("cppcheck").get("version", ""))

        errors_elem = ET.SubElement(new_root, "errors")
        for error in filtered_errors:
            errors_elem.append(error)

        # Write filtered results
        filtered_tree = ET.ElementTree(new_root)
        filtered_tree.write(output_file, encoding="utf-8", xml_declaration=True)

        print(f"Found {len(filtered_errors)} issues in changed lines")

        # Also print human-readable format
        for error in filtered_errors:
            severity = error.get("severity", "unknown")
            msg = error.get("msg", "")
            error_id = error.get("id", "")

            for location in error.findall("location"):
                file_path = location.get("file")
                line_num = location.get("line")
                print(f"{file_path}:{line_num}: {severity}: {msg} [{error_id}]")

        return len(filtered_errors)

    except Exception as e:
        print(f"Error filtering results: {e}")
        return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Filter cppcheck results for MISRA violations in changed lines"
    )
    parser.add_argument("--input", required=True, help="Path to cppcheck XML file")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument(
        "--git-diff",
        default="origin/main...HEAD",
        help="Git diff range (default: origin/main...HEAD)",
    )

    args = parser.parse_args()
    num_issues = filter_cppcheck_results(args.input, args.git_diff, args.output)
    print(f"Found {num_issues} misra violations")
    sys.exit(0)
