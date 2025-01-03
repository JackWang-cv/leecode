# source:https://leetcode.cn/problems/minimum-levels-to-gain-more-points/description/ 前缀和
from typing import List


class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        mn = 0
        mx = 0
        for i in possible:
            mx += 1 if i else -1
        res = 0
        for i in range(len(possible)-1):
            mn += 1 if possible[i] else -1
            mx -= 1 if possible[i] else -1
            res += 1
            if mn > mx:
                return res
        return -1