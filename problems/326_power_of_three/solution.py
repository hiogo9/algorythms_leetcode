#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
from typing import *
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            n = n / 3  # type: ignore cos im lazy shit
        if n == 1:
            return True
        else:
            return False


# @lc code=end
