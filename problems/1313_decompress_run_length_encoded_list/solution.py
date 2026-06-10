#
# @lc app=leetcode id=1313 lang=python3
#
# [1313] Decompress Run-Length Encoded List
#

# @lc code=start
from typing import *


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums), 2):
            result = result + [nums[i + 1]] * nums[i]
        return result


# @lc code=end
