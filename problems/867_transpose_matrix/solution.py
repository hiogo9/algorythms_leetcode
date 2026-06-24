#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#

# @lc code=start
from typing import *


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        ans = []
        for j in range(n_cols):
            t_row = []
            for i in range(n_rows):
                t_row.append(matrix[i][j])
            ans.append(t_row)
        return ans


# @lc code=end
