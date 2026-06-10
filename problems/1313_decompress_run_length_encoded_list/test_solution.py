import pytest
from solution import Solution


@pytest.mark.parametrize(
    "args, expected",
    [
        (([1, 2, 3, 4],), [2, 4, 4, 4]),
        (([1, 1, 2, 3],), [1, 3, 3]),
    ],
)
def test_solution(args, expected):
    assert Solution().decompressRLElist(*args) == expected
