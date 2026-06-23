#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#

# @lc code=start
from typing import *


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_1 = 0
        min_2 = 0
        for n in nums:
            if n >= min_1:
                min_2 = min_1
                min_1 = n
            elif n > min_2:
                min_2 = n
        return (min_1 - 1) * (min_2 - 1)


# @lc code=end
