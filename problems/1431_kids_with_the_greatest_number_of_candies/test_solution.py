import pytest
from solution import Solution

@pytest.mark.parametrize(
    "args, expected",
    [
        ((), ),
    ],
)
def test_solution(args, expected):
    assert Solution().kidsWithCandies(*args) == expected
