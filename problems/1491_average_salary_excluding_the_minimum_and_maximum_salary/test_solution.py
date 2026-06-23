from solution3 import Solution3
from solution2 import Solution2
import pytest
from solution import Solution


@pytest.mark.parametrize(
    "args, expected",
    [
        (([4000, 3000, 1000, 2000],), 2500.00000),
        (([1000, 2000, 3000],), 2000.00000),
    ],
)
def test_solution(args, expected):
    assert Solution().average(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [
        (([4000, 3000, 1000, 2000],), 2500.00000),
        (([1000, 2000, 3000],), 2000.00000),
    ],
)
def test_solution2(args, expected):
    assert Solution2().average(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [
        (([4000, 3000, 1000, 2000],), 2500.00000),
        (([1000, 2000, 3000],), 2000.00000),
    ],
)
def test_solution3(args, expected):
    assert Solution3().average(*args) == expected
