#
# @lc app=leetcode id=1491 lang=python3
#
# [1491] Average Salary Excluding the Minimum and Maximum Salary
#

# @lc code=start
from typing import *


class Solution:
    def average(self, salary: List[int]) -> float:
        summ = 0
        lenn = 0
        minn = float("inf")
        maxx = -float("inf")
        for s in salary:
            summ += s
            lenn += 1
            if s > maxx:
                maxx = s
            if s < minn:
                minn = s

        return (summ - minn - maxx) / (lenn - 2)


# @lc code=end
