from solution2 import Solution2
import pytest
from solution import Solution


@pytest.mark.parametrize(
    "args, expected",
    [
        ((["--X", "X++", "X++"],), 1),
        ((["++X", "++X", "X++"],), 3),
    ],
)
def test_solution(args, expected):
    assert Solution().finalValueAfterOperations(*args) == expected


@pytest.mark.parametrize(
    "args, expected",
    [
        ((["--X", "X++", "X++"],), 1),
        ((["++X", "++X", "X++"],), 3),
    ],
)
def test_solution2(args, expected):
    assert Solution2().finalValueAfterOperations(*args) == expected
