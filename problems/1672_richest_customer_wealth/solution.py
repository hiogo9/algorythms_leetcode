#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
from typing import *


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = 0
        for customer in accounts:
            maximum = sum(customer)
            result = max(result, maximum)
        return result


# @lc code=end
