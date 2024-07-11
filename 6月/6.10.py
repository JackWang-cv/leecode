# source:https://leetcode.cn/problems/boats-to-save-people/description/
from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        L = sorted(people)
        i = 0
        heavy = len(L)-1
        count = 0
        while i<=heavy:
            if L[i]+L[heavy]>limit:
                heavy -= 1
            else:
                i += 1
                heavy -= 1
            count += 1
        return count