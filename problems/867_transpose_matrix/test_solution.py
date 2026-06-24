import pytest
from solution import Solution


@pytest.mark.parametrize(
    "args, expected",
    [
        (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), [[1, 4, 7], [2, 5, 8], [3, 6, 9]]),
        (([[1, 2, 3], [4, 5, 6]],), [[1, 4], [2, 5], [3, 6]]),
    ],
)
def test_solution(args, expected):
    assert Solution().transpose(*args) == expected
