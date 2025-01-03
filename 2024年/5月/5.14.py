from collections import Counter
from typing import List
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = Counter(tasks)
        res = 0
        for v in cnt.values():
            if v == 1:
                return -1
            if v % 3 == 0:
                res += v // 3
            else:
                res += (1 + v // 3)
        return res


""" 这个复杂度O(n2)超时
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = set(tasks)
        count = []
        res = 0
        for i in cnt:
            v = tasks.count(i)
            if v==1:
                return -1
            if v % 3 == 0:
                res += v//3
            else:
                res += (1 + v//3)
        return res
"""
