#
# @lc app=leetcode id=2011 lang=python3
#
# [2011] Final Value of Variable After Performing Operations
#
from typing import *


# @lc code=start
class Solution2:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum([1 if "+" in o else -1 for o in operations])


# @lc code=end
