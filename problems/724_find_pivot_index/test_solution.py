import pytest
from solution import Solution


@pytest.mark.parametrize(
    "args, expected",
    [
        (([1, 7, 3, 6, 5, 6],), 3),
        (([1, 2, 3],), -1),
        (([2, 1, -1],), 0),
    ],
)
def test_solution(args, expected):
    assert Solution().pivotIndex(*args) == expected
