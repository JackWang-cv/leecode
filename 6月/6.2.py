# source:https://leetcode.cn/problems/distribute-candies/
from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        eat = len(candyType) // 2
        L = set(candyType)
        if len(L) >  eat:
            return eat
        else:
            return len(L)