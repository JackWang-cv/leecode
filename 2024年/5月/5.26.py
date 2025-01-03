# source: https://leetcode.cn/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        flag = False
        while i < len(strs[0]):
            temp = strs[0][i]
            for j in range(1, len(strs)):
                if i>=len(strs[j]):
                    flag = True
                    break
                if strs[j][i] != temp:
                    flag = True
            if flag:
                break
            i += 1
        return strs[0][:i]