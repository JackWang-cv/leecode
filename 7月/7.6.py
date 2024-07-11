# source:https://leetcode.cn/problems/count-alternating-subarrays/description/ 贪心
from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        res = cur = 0
        pre = -1
        for a in nums:
            if pre != a:
                cur += 1
            else:
                cur = 1
            pre = a
            res += cur
        return res