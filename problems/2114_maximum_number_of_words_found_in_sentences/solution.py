#
# @lc app=leetcode id=2114 lang=python3
#
# [2114] Maximum Number of Words Found in Sentences
#
from typing import *
# @lc code=start
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for s in sentences:
            cur_len = len(s.split(" "))
            if cur_len > ans: 
                ans = cur_len
        return ans
# @lc code=end

