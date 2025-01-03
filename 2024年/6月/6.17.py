# source:https://leetcode.cn/problems/longest-uncommon-subsequence-ii/  枚举
from typing import List


class Solution:
    def judge(self, s, t):
        L1 = len(s)
        L2 = len(t)
        j = 0
        for i in range(L1):
            if s[i] == t[j]:
                i += 1
                j += 1
            if j == L2:
                return 1
        return 0

    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=lambda s: -len(s))
        store = []
        temp = set()

        for i in range(len(strs)):
            t = strs[i]
            for j in range(len(strs)):
                if j != i and self.judge(strs[j], t):
                    break
            else:
                return len(t)
        return -1