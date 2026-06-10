from solution2 import Solution2
import pytest
from solution import Solution


@pytest.mark.parametrize(
    "args, expected",
    [
        (([[1, 2, 3], [3, 2, 1]],), 6),
        (([[1, 5], [7, 3], [3, 5]],), 10),
        (([[2, 8, 7], [7, 1, 3], [1, 9, 5]],), 17),
    ],
)
def test_solution(args, expected):
    assert Solution().maximumWealth(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [
        (([[1, 2, 3], [3, 2, 1]],), 6),
        (([[1, 5], [7, 3], [3, 5]],), 10),
        (([[2, 8, 7], [7, 1, 3], [1, 9, 5]],), 17),
    ],
)
def test_solution2(args, expected):
    assert Solution2().maximumWealth(*args) == expected
