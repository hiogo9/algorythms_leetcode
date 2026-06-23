import pytest
from solution import Solution


@pytest.mark.parametrize(
    "args, expected",
    [
        (([1, 0, 0, 0, 1], 1), True),
        (([1, 0, 0, 0, 1], 2), False),
    ],
)
def test_solution(args, expected):
    assert Solution().canPlaceFlowers(*args) == expected
