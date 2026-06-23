import pytest
from solution import Solution


@pytest.mark.parametrize(
    "args, expected",
    [
        (([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]],), True),
        (([[1, 2], [2, 2]],), False),
    ],
)
def test_solution(args, expected):
    assert Solution().isToeplitzMatrix(*args) == expected
