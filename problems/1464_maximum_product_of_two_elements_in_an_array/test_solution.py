import pytest
from solution import Solution


@pytest.mark.parametrize(
    "args, expected",
    [
        (([3, 4, 5, 2],), 12),
        (([1, 5, 4, 5],), 16),
        (([3, 7],), 12),
    ],
)
def test_solution(args, expected):
    assert Solution().maxProduct(*args) == expected
