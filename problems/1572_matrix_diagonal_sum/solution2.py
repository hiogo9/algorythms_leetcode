#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#

# @lc code=start
from typing import *


class Solution2:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        n = len(mat)
        c = 0

        for r in range(n):
            ans += mat[r][c]
            c += 1
        c = n - 1

        for r in range(n):
            if r != c:
                ans += mat[r][c]
            c -= 1
        return ans


# 2n
# @lc code=end
