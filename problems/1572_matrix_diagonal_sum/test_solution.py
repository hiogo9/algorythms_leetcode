from solution2 import Solution2
import pytest
from solution import Solution


@pytest.mark.parametrize(
    "args, expected",
    [
        (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), 25),
        (([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],), 8),
    ],
)
def test_solution(args, expected):
    assert Solution().diagonalSum(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [
        (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), 25),
        (([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],), 8),
    ],
)
def test_solution2(args, expected):
    assert Solution2().diagonalSum(*args) == expected
