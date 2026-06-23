#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
from typing import *


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zeros = 1
        ans = 0
        for f in flowerbed:
            if f == 0:
                zeros += 1
            else:
                if zeros % 2 != 0:
                    ans += zeros // 2
                else:
                    ans += (zeros // 2) - 1
                zeros = 0
        ans += zeros // 2
        return ans >= n


# @lc code=end
