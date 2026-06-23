import pytest
from solution import Solution


@pytest.mark.parametrize(
    "args, expected",
    [
        (("III"),),
    ],
)
def test_solution(args, expected):
    assert Solution().romanToInt(*args) == expected
