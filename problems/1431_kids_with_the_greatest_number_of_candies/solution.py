#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
from typing import *


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []
        for c in candies:
            if c + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result


# @lc code=end
