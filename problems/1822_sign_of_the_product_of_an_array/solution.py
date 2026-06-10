#
# @lc app=leetcode id=1822 lang=python3
#
# [1822] Sign of the Product of an Array
#

# @lc code=start
from typing import *


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                count += 1
        return -1 if count % 2 == 1 else 1


# @lc code=end
