# source:https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/ 二分+贪心 这道题第一次没贪好，写了两小时白费了。
# 结论：从小到大排序后，如果存在 k 对匹配，那么一定可以让最小的 k 个数和最大的 k 个数匹配
from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) // 2   # 开区间
        while left  < right:
            k = (left + right +1) // 2
            if all(nums[i] * 2 <= nums[i - k] for i in range(k)):
                left = k
            else:
                right = k-1
        return left * 2