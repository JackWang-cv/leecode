# source:https://leetcode.cn/problems/final-prices-with-a-special-discount-in-a-shop/ 单调栈
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                t = stack.pop()
                prices[t] -= prices[i]
            stack.append(i)
        return prices

# source:https://leetcode.cn/problems/next-greater-element-ii/ 单调栈
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        count = i = 0  # 2 * len(nums) - 1
        ans = [-1 for _ in range(len(nums))]
        stack = []
        while count < 2*len(nums)-1:
            if i == len(nums):
                i = 0
            while stack and nums[stack[-1]] < nums[i]:
                t = stack.pop()
                ans[t] = nums[i] 
            stack.append(i)
            count += 1
            i += 1
            
        return ans