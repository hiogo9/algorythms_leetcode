#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
from typing import *


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxx = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = maxx
            maxx = max(maxx, temp)
        return arr


# @lc code=end
