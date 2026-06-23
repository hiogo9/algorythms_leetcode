import pytest
from solution import Solution


@pytest.mark.parametrize(
    "args, expected",
    [
        (([2, 3, 5, 1, 3], 3), [True, True, True, False, True]),
        (([4, 2, 1, 1, 2], 1), [True, False, False, False, False]),
        (([12, 1, 12], 10), [True, False, True]),
    ],
)
def test_solution(args, expected):
    assert Solution().kidsWithCandies(*args) == expected
