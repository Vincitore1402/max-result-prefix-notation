from typing import Dict, Optional, Tuple
from itertools import product


class CalculationException(BaseException):
    pass


class InvalidExpressionException(CalculationException):
    pass


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()


ops = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x // y,
}


def is_operand(item):
    return item not in list(ops.keys())


def get_variables_combinations(
    variables_dict: Dict[str, Tuple[int, int]]
) -> [Dict[str, int]]:
    """
    Gets a list of possible variables combinations
    :param variables_dict: {"x": (4, 6), "y": (3,5)}
    :return: possible combinations list: [{"x": 4, "y": 3}, {"x": 4, "y": 4}, {"x": 5, "y": 3}, {"x": 5, "y": 4}]
    """
    variables_ranges_dict = {}

    for key in variables_dict.keys():
        value = variables_dict[key]

        if type(value) is tuple:
            variables_ranges_dict[key] = list(range(value[0], value[1]))

        else:
            variables_ranges_dict[key] = [value]

    names = variables_ranges_dict.keys()
    values = variables_ranges_dict.values()

    return [dict(zip(names, it)) for it in product(*values)]


def parse_expression(expression: str) -> []:
    """
    Parses the initial expression and validates it.
    In case of any bad result raises an InvalidExpressionException
    :param expression: "+ 2 5"
    :return: parsed expression: ["5" "2" "+"]
    """
    expression_items = expression.split(" ")

    formatted_expression = [string for string in expression_items if string != ""][::-1]

    operands_symbols_size = len([it for it in formatted_expression if is_operand(it)])
    operation_symbols_size = len(formatted_expression) - operands_symbols_size

    if (
        len(formatted_expression) == 0
        or operation_symbols_size == 0
        or operands_symbols_size == 0
        or operands_symbols_size - operation_symbols_size != 1
    ):
        raise InvalidExpressionException("Invalid expression")

    return formatted_expression


def prefix_expression(
    expression: [str], expression_variables: Dict
) -> int:
    """
    Evaluates the prefix expression
    :param expression:
    :param expression_variables:
    """
    stack = Stack()

    for item in expression:
        if is_operand(item):
            operand = int(item) if item.isdigit() else expression_variables[item]

            if type(item) == "float" or operand < 0:
                raise InvalidExpressionException(
                    "Expression numbers should be positive integers"
                )

            stack.push(operand)
        else:
            item1 = stack.pop()
            item2 = stack.pop()

            operation_func = ops[item]

            stack.push(operation_func(item1, item2))

    return stack.pop()


def max_result_expression(
    expression: str, variables: Dict[str, Tuple[int, int]]
) -> Optional[int]:
    """
    Evaluates the prefix expression and calculates the maximum result for the given variable ranges.

    Arguments:
        expression: the prefix expression to evaluate.
        variables: Keys of this dictionary may appear as variables in the expression.
            Values are tuples of `(min, max)` that specify the range of values of the variable.
            The upper bound `max` is NOT included in the range, so (2, 5) expands to [2, 3, 4].

    Returns:
        int:  the maximum result of the expression for any combination of the supplied variables.
        None: in the case there is no valid result for any combination of the supplied variables.
    """

    try:
        parsed_expression = parse_expression(expression)

        variables_combinations = get_variables_combinations(variables)

        max_result = max(
            [
                prefix_expression(parsed_expression, it)
                for it in variables_combinations
            ]
        )

        return max_result
    except CalculationException:
        return None


if __name__ == "__main__":
    user_expression = str(input())
    user_variables = eval(input())

    calculation_result = max_result_expression(user_expression, user_variables)

    print(calculation_result)
