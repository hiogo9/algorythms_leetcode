import pytest
from solution import Solution


@pytest.mark.parametrize(
    "args, expected",
    [
        (([-1, -2, -3, -4, 3, 2, 1],), 1),
        (([1, 5, 0, 2, -3],), 0),
        (([-1, 1, -1, 1, -1],), -1),
    ],
)
def test_solution(args, expected):
    assert Solution().arraySign(*args) == expected
