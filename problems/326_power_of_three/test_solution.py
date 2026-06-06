import pytest
from solution import Solution


@pytest.mark.parametrize(
    "args, expected",
    [
        ((27,), True),
        ((0,), False),
    ],
)
def test_solution(args, expected):
    assert Solution().isPowerOfThree(*args) == expected
