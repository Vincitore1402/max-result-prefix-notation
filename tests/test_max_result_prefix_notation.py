from max_result_prefix_notation import max_result_expression, get_variables_combinations

from max_result_prefix_notation.utils.common_utils import arrays_difference


def test_get_variables_combinations():
    combinations = get_variables_combinations({"x": (0, 2), "y": (2, 4)})

    expected_result = [
        {"x": 0, "y": 2},
        {"x": 0, "y": 3},
        {"x": 1, "y": 2},
        {"x": 1, "y": 3},
    ]

    assert arrays_difference(combinations, expected_result) == []
    assert arrays_difference(get_variables_combinations({}), [{}]) == []


def test_basic_prefix_notation():
    assert max_result_expression("+ 2 5", {}) == 7
    assert max_result_expression("* + 1 2 3", {}) == 9
    assert max_result_expression("- * + 1 2 3 4", {}) == 5
    assert max_result_expression("+ 6 * - 4 + 2 3 8", {}) == -2
    assert max_result_expression("+ 1                       2", {}) == 3


def test_invalid_values():
    assert max_result_expression("+ 1 2 3", {}) is None
    assert max_result_expression("+ 1", {}) is None
    assert max_result_expression("9", {}) is None
    assert max_result_expression("-+1 5 3", {}) is None
    assert max_result_expression("+ * 7 x z / 5", {"x": (5, 14), "z": (0, 3)}) is None
    assert max_result_expression("", {}) is None
    assert max_result_expression("", {"x": (1, -5)}) is None
    assert max_result_expression("+ x            x", {"x": (1, -5)}) is None
    assert max_result_expression("+ x            x", {"x": (-9, -5)}) is None


def test_prefix_notation_with_variables():
    assert max_result_expression("* + 2 x y", {"x": (0, 2), "y": (2, 4)}) == 9
    assert max_result_expression("+ + 10 x y", {"x": (3, 4), "y": (0, 1)}) == 13
    assert max_result_expression("+ 10 x", {"x": (3, 7)}) == 16
