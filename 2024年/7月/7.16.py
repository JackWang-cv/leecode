# source:https://leetcode.cn/problems/132-pattern/description/ 二分

from typing import List
from bisect import bisect_right
from sortedcontainers import SortedList


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        leftmin = nums[0]
        right_all = SortedList(nums[2:])
        for i in range(1,len(nums)-1):
            temp = nums[i]
            index = bisect_right(right_all, leftmin)
            if index < len(right_all) and right_all[index] < temp:
                return True
            leftmin = min(leftmin, temp)
            right_all.remove(nums[i+1])
        return False
