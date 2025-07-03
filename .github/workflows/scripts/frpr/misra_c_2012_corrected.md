# MISRA C 2012 Rules - Complete Reference

## Rules Summary by Category

### Directive 1: Language

| Rule | Category | Description |
|------|----------|-------------|
| 1.1 | Required | The program shall contain no violations of the standard C syntax and constraints and shall not exceed the implementation's translation limits |
| 1.2 | Advisory | Language extensions should not be used |
| 1.3 | Required | There shall be no occurrence of undefined or critical unspecified behavior |

### Directive 2: Unused Code

| Rule | Category | Description |
|------|----------|-------------|
| 2.1 | Required | A project shall not contain unreachable code |
| 2.2 | Required | There shall be no dead code |
| 2.3 | Advisory | A project should not contain unused type declarations |
| 2.4 | Advisory | A project should not contain unused tag declarations |
| 2.5 | Advisory | A project should not contain unused macro declarations |
| 2.6 | Advisory | A function should not contain unused label declarations |
| 2.7 | Advisory | There should be no unused parameters in functions |

### Directive 3: Comments

| Rule | Category | Description |
|------|----------|-------------|
| 3.1 | Required | The character sequences /* and // shall not be used within a comment |
| 3.2 | Required | Line-splicing shall not be used in // comments |

### Directive 4: Character Sets

| Rule | Category | Description |
|------|----------|-------------|
| 4.1 | Required | Octal and hexadecimal escape sequences shall be terminated |
| 4.2 | Advisory | Trigraphs should not be used |

### Directive 5: Identifiers

| Rule | Category | Description |
|------|----------|-------------|
| 5.1 | Required | External identifiers shall be distinct |
| 5.2 | Required | Identifiers declared in the same scope and name space shall be distinct |
| 5.3 | Required | An identifier declared in an inner scope shall not hide an identifier declared in an outer scope |
| 5.4 | Required | Macro identifiers shall be distinct |
| 5.5 | Required | Identifiers shall be distinct from macro names |
| 5.6 | Required | A typedef name shall be a unique identifier |
| 5.7 | Required | A tag name shall be a unique identifier |

### Directive 6: Types

| Rule | Category | Description |
|------|----------|-------------|
| 6.1 | Required | Bit-fields shall only be declared with an appropriate type |
| 6.2 | Required | Single-bit named bit fields shall not be of a signed type |

### Directive 7: Literals

| Rule | Category | Description |
|------|----------|-------------|
| 7.1 | Required | Octal constants shall not be used |
| 7.2 | Required | A u or U suffix shall be applied to all integer constants that are represented in an unsigned type |
| 7.3 | Required | The lowercase character l shall not be used in a literal suffix |
| 7.4 | Required | A string literal shall not be assigned to an object unless the object's type is pointer to const-qualified char |

### Directive 8: Declarations and Definitions

| Rule | Category | Description |
|------|----------|-------------|
| 8.1 | Required | Types shall be explicitly specified |
| 8.2 | Required | Function types shall be in prototype form with named parameters |
| 8.3 | Required | All declarations of an object or function shall use the same names and type qualifiers |
| 8.4 | Required | A compatible declaration shall be visible when an object or function with external linkage is defined |
| 8.5 | Required | An external object or function shall be declared once in one and only one file |
| 8.6 | Required | An identifier with external linkage shall have exactly one external definition |
| 8.7 | Advisory | Functions and objects should not be defined with external linkage if they are referenced in only one translation unit |
| 8.8 | Required | The static storage class specifier shall be used in all declarations of objects and functions that have internal linkage |
| 8.9 | Advisory | An object should be defined at block scope if its identifier only appears in a single function |
| 8.10 | Required | An inline function shall be declared with the static storage class |
| 8.11 | Advisory | When an array with external linkage is declared its size should be explicitly specified |
| 8.12 | Required | Within an enumerator list the value of an implicitly-specified enumeration constant shall be unique |
| 8.13 | Advisory | A pointer should point to a const-qualified type whenever possible |
| 8.14 | Required | The restrict type qualifier shall not be used |

### Directive 9: Initialization

| Rule | Category | Description |
|------|----------|-------------|
| 9.1 | Mandatory | The value of an object with automatic storage duration shall not be read before it has been set |
| 9.2 | Required | The initializer for an aggregate or union shall be enclosed in braces |
| 9.3 | Required | Arrays shall not be partially initialized |
| 9.4 | Required | An element of an object shall not be initialized more than once |
| 9.5 | Required | Where designated initializers are used to initialize an array object the size of the array shall be specified explicitly |

### Directive 10: Essential Type Model

| Rule | Category | Description |
|------|----------|-------------|
| 10.1 | Required | Operands shall not be of an inappropriate essential type |
| 10.2 | Required | Expressions of essentially character type shall not be used inappropriately in addition and subtraction operations |
| 10.3 | Required | The value of an expression shall not be assigned to an object with a narrower essential type or of a different essential type category |
| 10.4 | Required | Both operands of an operator in which the usual arithmetic conversions are performed shall have the same essential type category |
| 10.5 | Advisory | The value of an expression should not be cast to an inappropriate essential type |
| 10.6 | Required | The value of a composite expression shall not be assigned to an object with wider essential type |
| 10.7 | Required | If a composite expression is used as one operand of an operator in which the usual arithmetic conversions are performed then the other operand shall not have wider essential type |
| 10.8 | Required | The value of a composite expression shall not be cast to a different essential type category or a wider essential type |

### Directive 11: Pointer Type Conversions

| Rule | Category | Description |
|------|----------|-------------|
| 11.1 | Required | Conversions shall not be performed between a pointer to a function and any other type |
| 11.2 | Required | Conversions shall not be performed between a pointer to an incomplete type and any other type |
| 11.3 | Required | A cast shall not be performed between a pointer to object type and a pointer to a different object type |
| 11.4 | Advisory | A conversion should not be performed between a pointer to object and an integer type |
| 11.5 | Advisory | A conversion should not be performed from pointer to void into pointer to object |
| 11.6 | Required | A cast shall not be performed between pointer to void and an arithmetic type |
| 11.7 | Required | A cast shall not be performed between pointer to object and a non-integer arithmetic type |
| 11.8 | Required | A cast shall not remove any const or volatile qualification from the type pointed to by a pointer |
| 11.9 | Required | The macro NULL shall be the only permitted form of integer null pointer constant |

### Directive 12: Expressions

| Rule | Category | Description |
|------|----------|-------------|
| 12.1 | Advisory | The precedence of operators within expressions should be made explicit |
| 12.2 | Required | The right hand operand of a shift operator shall lie in the range zero to one less than the width in bits of the essential type of the left hand operand |
| 12.3 | Advisory | The comma operator should not be used |
| 12.4 | Advisory | Evaluation of constant expressions should not lead to unsigned integer wrap-around |
| 12.5 | Mandatory | The sizeof operator shall not have an operand which is a function parameter declared as array type |

### Directive 13: Side Effects

| Rule | Category | Description |
|------|----------|-------------|
| 13.1 | Required | Initializer lists shall not contain persistent side effects |
| 13.2 | Required | The value of an expression and its persistent side effects shall be the same under all permitted evaluation orders |
| 13.3 | Advisory | A full expression containing an increment (++) or decrement (--) operator should have no other potential side effects other than that caused by the increment or decrement operator |
| 13.4 | Advisory | The result of an assignment operator should not be used |
| 13.5 | Required | The right hand operand of a logical && or \|\| operator shall not contain persistent side effects |
| 13.6 | Mandatory | The operand of the sizeof operator shall not contain any expression which has potential side effects |

### Directive 14: Control Statement Expressions

| Rule | Category | Description |
|------|----------|-------------|
| 14.1 | Required | A loop counter shall not have essentially floating type |
| 14.2 | Required | A for loop shall be well-formed |
| 14.3 | Required | Controlling expressions shall not be invariant |
| 14.4 | Required | The controlling expression of an if statement and the controlling expression of an iteration-statement shall have essentially Boolean type |

### Directive 15: Control Flow

| Rule | Category | Description |
|------|----------|-------------|
| 15.1 | Advisory | The goto statement should not be used |
| 15.2 | Required | The goto statement shall jump to a label declared later in the same function |
| 15.3 | Required | Any label referenced by a goto statement shall be declared in the same block or in any block enclosing the goto statement |
| 15.4 | Advisory | There should be no more than one break or goto statement used to terminate any iteration statement |
| 15.5 | Advisory | A function should have a single point of exit at the end |
| 15.6 | Required | The body of an iteration-statement or a selection-statement shall be a compound-statement |
| 15.7 | Required | All if else if constructs shall be terminated with an else statement |

### Directive 16: Switch Statements

| Rule | Category | Description |
|------|----------|-------------|
| 16.1 | Required | All switch statements shall be well-formed |
| 16.2 | Required | A switch label shall only be used when the most closely-enclosing compound statement is the body of a switch statement |
| 16.3 | Required | An unconditional break statement shall terminate every switch-clause |
| 16.4 | Required | Every switch statement shall have a default label |
| 16.5 | Required | A default label shall appear as either the first or the last switch label of a switch statement |
| 16.6 | Required | Every switch statement shall have at least two switch-clauses |
| 16.7 | Required | A switch-expression shall not have essentially Boolean type |

### Directive 17: Functions

| Rule | Category | Description |
|------|----------|-------------|
| 17.1 | Required | The features of <stdarg.h> shall not be used |
| 17.2 | Required | Functions shall not call themselves either directly or indirectly |
| 17.3 | Mandatory | A function shall not be declared implicitly |
| 17.4 | Mandatory | All exit paths from a function with non-void return type shall have an explicit return statement with an expression |
| 17.5 | Advisory | The function argument corresponding to a parameter declared to have an array type shall have an appropriate number of elements |
| 17.6 | Mandatory | The declaration of an array parameter shall not contain the static keyword between the [ ] |
| 17.7 | Required | The value returned by a function having non-void return type shall be used |
| 17.8 | Advisory | A function parameter should not be modified |

### Directive 18: Pointers and Arrays

| Rule | Category | Description |
|------|----------|-------------|
| 18.1 | Required | A pointer resulting from arithmetic on a pointer operand shall address an element of the same array as that pointer operand |
| 18.2 | Required | Subtraction between pointers shall only be applied to pointers that address elements of the same array |
| 18.3 | Required | The relational operators > >= < and <= shall not be applied to objects of pointer type except where they point into the same object |
| 18.4 | Advisory | The + - += and -= operators should not be applied to an expression of pointer type |
| 18.5 | Advisory | Declarations should contain no more than two levels of pointer nesting |
| 18.6 | Required | The address of an object with automatic storage shall not be copied to another object that persists after the first object has ceased to exist |
| 18.7 | Required | Flexible array members shall not be declared |
| 18.8 | Required | Variable-length array types shall not be used |

### Directive 19: Overlapping Storage

| Rule | Category | Description |
|------|----------|-------------|
| 19.1 | Mandatory | An object shall not be assigned or copied to an overlapping object |
| 19.2 | Advisory | The union keyword should not be used |

### Directive 20: Preprocessing Directives

| Rule | Category | Description |
|------|----------|-------------|
| 20.1 | Advisory | #include directives should only be preceded by preprocessor directives or comments |
| 20.2 | Required | The ' " or \ characters and the /* or // character sequences shall not occur in a header file name |
| 20.3 | Required | The #include directive shall be followed by either a <filename> or "filename" sequence |
| 20.4 | Required | A macro shall not be defined with the same name as a keyword |
| 20.5 | Advisory | #undef should not be used |
| 20.6 | Required | Tokens that look like a preprocessing directive shall not occur within a macro argument |
| 20.7 | Required | Expressions resulting from the expansion of macro parameters shall be enclosed in parentheses |
| 20.8 | Required | The controlling expression of a #if or #elif preprocessing directive shall evaluate to 0 or 1 |
| 20.9 | Required | All identifiers used in the controlling expression of #if or #elif preprocessing directives shall be #define'd before evaluation |
| 20.10 | Advisory | The # and ## preprocessor operators should not be used |
| 20.11 | Required | A macro parameter immediately following a # operator shall not immediately be followed by a ## operator |
| 20.12 | Required | A macro parameter used as an operand to the # or ## operators which is itself subject to further macro replacement shall only be used as an operand to these operators |
| 20.13 | Required | A line whose first token is # shall be a valid preprocessing directive |
| 20.14 | Required | All #else #elif and #endif preprocessor directives shall reside in the same file as the #if #ifdef or #ifndef directive to which they are related |

### Directive 21: Standard Library

| Rule | Category | Description |
|------|----------|-------------|
| 21.1 | Required | #define and #undef shall not be used on a reserved identifier or reserved macro name |
| 21.2 | Required | A reserved identifier or reserved macro name shall not be declared |
| 21.3 | Required | The memory allocation and deallocation functions of <stdlib.h> shall not be used |
| 21.4 | Required | The standard header file <setjmp.h> shall not be used |
| 21.5 | Required | The standard header file <signal.h> shall not be used |
| 21.6 | Required | The Standard Library input/output functions shall not be used |
| 21.7 | Required | The Standard Library functions atof atoi atol and atoll of <stdlib.h> shall not be used |
| 21.8 | Required | The Standard Library functions abort exit getenv and system of <stdlib.h> shall not be used |
| 21.9 | Required | The Standard Library functions bsearch and qsort of <stdlib.h> shall not be used |
| 21.10 | Required | The Standard Library time and date functions shall not be used |
| 21.11 | Required | The standard header file <tgmath.h> shall not be used |
| 21.12 | Advisory | The exception handling features of <fenv.h> should not be used |
| 21.13 | Mandatory | Any value passed to a function in <ctype.h> shall be representable as an unsigned char or be the value EOF |
| 21.14 | Required | The Standard Library function memcmp shall not be used to compare null terminated strings |
| 21.15 | Required | The pointer arguments to the Standard Library functions memcpy memmove and memcmp shall be pointers to qualified or unqualified versions of compatible types |
| 21.16 | Required | The pointer arguments to the Standard Library function memcmp shall point to either a pointer type an essentially signed type an essentially unsigned type an essentially Boolean type or an essentially enum type |
| 21.17 | Mandatory | Use of the string handling functions from <string.h> shall not result in accesses beyond the bounds of the objects referenced by their pointer parameters |
| 21.18 | Mandatory | The size_t argument passed to any function in <string.h> shall have an appropriate value |
| 21.19 | Mandatory | The pointers returned by the Standard Library functions localeconv getenv setlocale or strerror shall only be used as if they have pointer to const-qualified type |
| 21.20 | Mandatory | The pointer returned by the Standard Library functions asctime ctime gmtime localtime localeconv getenv setlocale or strerror shall not be used following a subsequent call to the same function |

### Directive 22: Resources

| Rule | Category | Description |
|------|----------|-------------|
| 22.1 | Required | All resources obtained dynamically by means of Standard Library functions shall be explicitly released |
| 22.2 | Mandatory | A block of memory shall only be freed if it was allocated by means of a Standard Library function |
| 22.3 | Required | The same file shall not be open for read and write access at the same time on different streams |
| 22.4 | Mandatory | There shall be no attempt to write to a stream which has been opened as read-only |
| 22.5 | Mandatory | A pointer to a FILE object shall not be dereferenced |
| 22.6 | Mandatory | The value of a pointer to a FILE shall not be used after the associated stream has been closed |
| 22.7 | Required | The macro EOF shall only be compared with the unmodified return value from any Standard Library function capable of returning EOF |
| 22.8 | Required | The value of errno shall be set to zero prior to a call to an errno-setting-function |
| 22.9 | Required | The value of errno shall be tested against zero after calling an errno-setting-function |
| 22.10 | Required | The value of errno shall only be tested when the last function to be called was an errno-setting-function |

## Summary

- **Total Rules**: 143
- **Required**: 98
- **Advisory**: 30
- **Mandatory**: 15
