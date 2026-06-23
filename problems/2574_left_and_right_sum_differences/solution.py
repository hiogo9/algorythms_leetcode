#
# @lc app=leetcode id=2574 lang=python3
#
# [2574] Left and Right Sum Differences
#

# @lc code=start
from typing import *


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right = sum(nums)
        left = 0
        ans = []
        for num in nums:
            ans.append(abs(left - (right - num)))
            left += num
            right -= num
        return ans


# @lc code=end
