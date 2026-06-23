import pytest
from solution import Solution


@pytest.mark.parametrize(
    "args, expected",
    [
        (([10, 4, 8, 3],), [15, 1, 11, 22]),
        (([1],), [0]),
    ],
)
def test_solution(args, expected):
    assert Solution().leftRightDifference(*args) == expected
