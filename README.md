# Phase-1
# Lexer Construction
In this assignment we wrote a DFA-based Lexical Analyser that recognizes some of the basic lexemes. A driver program(parser) is written that calls your Scanner repeatedly, returning each token found by the Scanner in the input stream.

## Requirements Specification:
|||
|---|---|
| Input | Program File (example shown at the end)
| Output | Return tokens either in the form of some number or as TK-identifier
| Side Effects | White spaces removed
| Exceptions | Invalid tokens

Our language reserves all the key words that can appear in the language.
## Scanner Deliverables
```
C/C++ Code for scanner.
Test cases and output files for test cases
```
## Scanner sample Test Suite
```
Formulate your own test set / programs from the token list given as examples. The test set to be
used for evaluation
```

## Token List
```
Keywords : int, float, boolean, string, while, until, if else, true, false

Operators : +, -, *, /, %, :=, ==, >, <, >=, <=, !=, &&, ||, !, ?, :

Delimiters : {, }, (, ), [, ], ;, ,

Identifiers : must start with a letter (upper or lower case), and may contain zero or more additional characters as long as they are letters, digits, or underscores

Integer Literals : may begin with an optional plus or minus followed by a sequence of one or more digits, provided that the first digit can only be zero for the number zero (which should not have a plus or minus before it).

Floating Point Literals : may begin with an optional plus or minus followed by a sequence of one or more digits with the same provision above for integers, followed by a decimal point and one or more digits after the decimal point.

String literals : start and end with a double quote followed by zero or more characters that may not be newlines, carriage returns, double quotes, or backslashes. The only exceptons are reserved escape sequences which are limited to the following: \t, \n, \r, \", and \\.
```
