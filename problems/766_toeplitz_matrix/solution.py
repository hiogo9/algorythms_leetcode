#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#

# @lc code=start
from typing import *


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m - 1):
            for j in range(n - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True


# @lc code=end
