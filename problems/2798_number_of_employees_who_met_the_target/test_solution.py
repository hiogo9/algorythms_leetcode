import pytest
from solution import Solution


@pytest.mark.parametrize(
    "args, expected",
    [
        (([0, 1, 2, 3, 4], 2), 3),
        (([5, 1, 4, 2, 2], 6), 0),
    ],
)
def test_solution(args, expected):
    assert Solution().numberOfEmployeesWhoMetTarget(*args) == expected
