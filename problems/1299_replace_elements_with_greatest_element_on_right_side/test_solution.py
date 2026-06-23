import pytest
from solution import Solution


@pytest.mark.parametrize(
    "args, expected",
    [
        (([17, 18, 5, 4, 6, 1],), [18, 6, 6, 6, 1, -1]),
        (([400],), [-1]),
    ],
)
def test_solution(args, expected):
    assert Solution().replaceElements(*args) == expected
