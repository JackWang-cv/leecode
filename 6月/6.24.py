# source:https://leetcode.cn/problems/next-greater-element-ii/description/  单调栈
from typing import List

# 单调栈


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [-1] * n
        stk = list()

        for i in range(n * 2 - 1):
            while stk and nums[stk[-1]] < nums[i % n]:
                ret[stk.pop()] = nums[i % n]
            stk.append(i % n)

        return ret

# 暴力


class Solution1:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = []
        mx = len(nums)
        for i in range(len(nums)):
            c = 0
            j = i+1
            while c<mx:
                if j==len(nums):
                    j = 0
                if nums[j]>nums[i]:
                    res.append(nums[j])
                    break
                j += 1
                c += 1
            if c==mx:
                res.append(-1)
        return res
