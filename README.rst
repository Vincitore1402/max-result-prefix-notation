Max result of prefix notation
-----

""""""""""""""
Tech Stack:
""""""""""""""
* Python 3.8
* poetry (package manager)


Description
^^^^^^^^^^^^^

Polish notation (PN), also known as normal Polish notation (NPN),  Polish prefix notation or simply prefix notation, is a mathematical notation in which operators precede their operands, in contrast to the more common infix notation, in which operators are placed between operands. It does not need any parentheses as long as each operator has a fixed number of operands.


For example:

::

 Infix notation: 2 + 6

 Prefix notation: + 6 2

 Result: 8

::

 Infix notation: (1 + 2) * 3

 Prefix notation: * + 1 2 3

 Result: 9


::

 Infix notation: 7 + ((4 - (2 * 5)) * 12)

 Prefix notation: + 7 * - 4 + 2 5 12

 Result: 4

Task
^^^^^^^^^^^^^
In our case we would like our `max_result_expression` function to support also variables within the expression.

Another feature of our function is possibility to set variables either as a single value or as a range of possible values (upper bound is NOT included)

::

 expression: + 7 y
 variables: {"y": (5, 14)}
 result: 20

::

 expression: + * / 7 x z 5
 variables: {"x": (5, 14), "z": (0, 3)}
 result: 7


So the final task for us would be:

Implementing a function `max_result_expression(expression, variables)`
that takes as inputs:

* expression, a String containing an expression in prefix notation that might contain variables
* variables, a dictionary containing a range of values for each variable In the expression
and returns:

* the maximum result of the expression for any combination of the given variable values

* None if the expression is invalid or if the expression does not have any valid result.

Our syntax supports 4 operators: +, -, *, and /. These are the standard arithmetic operators.