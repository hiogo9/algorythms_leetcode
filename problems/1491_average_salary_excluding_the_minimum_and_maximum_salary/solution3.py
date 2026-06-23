#
# @lc app=leetcode id=1491 lang=python3
#
# [1491] Average Salary Excluding the Minimum and Maximum Salary
#

# @lc code=start
from typing import *


class Solution3:
    def average(self, salary: List[int]) -> float:
        min_sal = min(salary)
        max_sal = max(salary)
        return (sum(salary) - min_sal - max_sal) / (len(salary) - 2)


# @lc code=end
