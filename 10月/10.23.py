# source:
from cmath import inf
from typing import List
from sortedcontainers import SortedList
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        max_id, min_id = 0, 0
        for j in range(indexDifference, len(nums)):
            i = j - indexDifference
            if nums[max_id] < nums[i]:
                max_id = i
            elif nums[min_id] > nums[i]:
                min_id = i
            if nums[max_id] - nums[j] >= valueDifference:
                return [max_id, j]
            if nums[j] - nums[min_id] >= valueDifference:
                return [min_id, j]
        return [-1, -1]

# source:https://leetcode.cn/problems/minimum-sum-of-mountain-triplets-ii/
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        pre = [inf for _ in range(len(nums)+1)]
        for i in range(len(nums)):
            pre[i+1] = min(pre[i], nums[i])
        suf = [inf for _ in range(len(nums)+1)]
        for i in range(len(nums)-1, -1, -1):
            suf[i] = min(suf[i+1], nums[i])
        # print(pre, suf)
        ans = inf
        for i in range(len(nums)):
            if nums[i]>pre[i+1] and nums[i]>suf[i+1]:
                ans = min(ans, pre[i+1]+suf[i]+nums[i])
        return ans if ans != inf else -1