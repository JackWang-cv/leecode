# source:https://leetcode.cn/problems/split-array-into-maximum-number-of-subarrays/
from cmath import inf
from typing import List


class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        mn = inf
        count = 0
        last = 0xffffffff
        for i in range(len(nums)):
            last &= nums[i]
            if last == 0:
                mn = 0
                count += 1
                last = 0xffffffff
        return count if count != 0 else 1
#11110 10010 10011 10100 1011 10101 1100 10110 11010