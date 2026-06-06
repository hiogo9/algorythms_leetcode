import pytest
from solution import Solution

@pytest.mark.parametrize("args, expected", [
    ((["alice and bob love leetcode", "i think so too", "this is great thanks very much"],), 6),
    ((["please wait", "continue to fight", "continue to win"],), 3)
])
def test_solution(args, expected):
    assert Solution().mostWordsFound(*args) == expected
