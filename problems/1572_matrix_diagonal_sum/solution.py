#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#

# @lc code=start
from typing import *


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        n = len(mat)
        c1 = 0
        c2 = n - 1
        for r in range(n):
            ans += mat[r][c1]
            if r != c2:
                ans += mat[r][c2]
            c1 += 1
            c2 -= 1
        return ans


# @lc code=end
