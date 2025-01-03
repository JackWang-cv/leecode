# source: https://leetcode.cn/problems/find-the-most-competitive-subsequence/ 单调栈
from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i, x in enumerate(nums):  # len(nums)-i+len(res)判断能不能继续往外弹，怕数组长度不够了，等会凑不齐K个
            while len(res) > 0 and len(nums) - i + len(res) > k and res[-1] > x:
                res.pop()
            res.append(x)
        return res[:k]

