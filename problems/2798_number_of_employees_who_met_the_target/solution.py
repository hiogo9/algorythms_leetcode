#
# @lc app=leetcode id=2798 lang=python3
#
# [2798] Number of Employees Who Met the Target
#
from typing import *


# @lc code=start
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ans = 0
        for h in hours:
            if h >= target:
                ans = ans + 1
        return ans


# @lc code=end
