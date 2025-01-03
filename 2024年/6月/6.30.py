# source:https://leetcode.cn/problems/target-sum/description/  回溯  或者 DP
from math import inf
from typing import List


class Solution:
    def __init__(self):
        self.target = 0
        self.nums = []
    def cal(self, i, s):
        if i==len(self.nums)-1:
            if s == self.target:
                return 1
            return 0
        return self.cal(i+1, s+self.nums[i+1]) + self.cal(i+1, s-self.nums[i+1])

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.target = target
        self.nums = nums
        return self.cal(0, self.nums[0]) + self.cal(0, (-1)*self.nums[0])

# source:https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/description/ 二分


class Solution1:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        i = 0
        j = len(nums) - 1
        mn = inf
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < mn:
                mn = nums[mid]
            if nums[i] < nums[mid] < nums[j]:
                j = mid - 1
            elif nums[i] > nums[mid] and nums[mid] < nums[j]:
                j = mid - 1
            else:
                i = mid + 1
        return mn