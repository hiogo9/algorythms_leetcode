import pytest
from solution import Solution


@pytest.mark.parametrize(
    "args, expected",
    [
        (([1, 1, 2, 1, 3],), 3),
        (([0, 1, 2],), 2),
    ],
)
def test_solution(args, expected):
    assert Solution().countTestedDevices(*args) == expected
