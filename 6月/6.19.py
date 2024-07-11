# source:https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/ 二分
from typing import List


class Solution:
    def find(self, left, right, target, nums):
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = set(nums)
        if target not in n:
            return [-1, -1]

        t1 = self.find(0, len(nums) - 1, target - 1, nums)
        t2 = self.find(0, len(nums) - 1, target + 1, nums)
        while nums[t1] != target:
            t1 += 1
        while nums[t2] != target:
            t2 -= 1
        return [t1, t2]
