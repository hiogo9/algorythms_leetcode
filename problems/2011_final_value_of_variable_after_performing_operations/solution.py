#
# @lc app=leetcode id=2011 lang=python3
#
# [2011] Final Value of Variable After Performing Operations
#
from typing import *


# @lc code=start
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for o in operations:
            if "+" in o:
                ans += 1
            else:
                ans -= 1
        return ans


# @lc code=end
