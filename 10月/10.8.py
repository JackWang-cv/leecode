# source:https://leetcode.cn/problems/count-the-number-of-beautiful-subarrays/ xor
from collections import defaultdict
from typing import List


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        ans = 0
        dit = defaultdict(int)
        for v in nums:
            ans ^= v
            dit[ans] += 1
        res = dit[0]
        for key in dit.keys():    
            res += (1 + dit[key]-1)*(dit[key]-1)//2
        return res

# source:https://leetcode.cn/problems/destination-city/description/ 哈希表
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        set_a = set()
        set_b = set()
        for a, b in paths:
            set_b.discard(a)  # a 一定不是答案
            if b not in set_a:  # b 有可能是答案
                set_b.add(b)
            set_a.add(a)
        return set_b.pop()
