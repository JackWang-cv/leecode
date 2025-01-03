# source:https://leetcode.cn/problems/valid-triangle-number/description/ 二分
from bisect import bisect_right
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        def find(L, target):
            i = 0
            j = len(L)-1
            while i<=j:
                mid = (i+j)//2
                if target<=L[mid]:
                    j = mid-1
                elif L[mid]<target:
                    i = mid+1
            return i
        nums.sort()
        res = 0
        for i in range(len(nums)-2):
            t = nums[i+2:]
            for j in range(i+1, len(nums)-1):
                num_two = nums[i]+nums[j]
                index = find(t, num_two)
                res += index
                t.remove(nums[j+1])
        return res