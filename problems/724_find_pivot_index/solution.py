#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
from typing import *


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            if left == right - nums[i]:
                return i
            left += nums[i]
            right -= nums[i]
        return -1


# @lc code=end
