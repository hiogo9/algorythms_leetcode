import pytest
from solution import Solution

@pytest.mark.parametrize("args, expected", [
    (("1.1.1.1",), "1[.]1[.]1[.]1"),
])
def test_solution(args, expected):
    assert Solution().defangIPaddr(*args) == expected

