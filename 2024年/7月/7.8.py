# source:https://leetcode.cn/problems/find-pivot-index/description/ 前缀和
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_l = 0
        sum_r = sum(nums)
        if len(nums) == 1:
            return 0

        for i in range(len(nums)):
            sum_r -= nums[i]
            if i - 1 >= 0:
                sum_l += nums[i - 1]
            if sum_r == sum_l:
                return i
        return -1

# source:https://leetcode.cn/problems/intersection-of-two-arrays-ii/description/  哈希表


class Solution1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = dict()
        d2 = dict()
        for i in nums1:
            d1[i] = d1.get(i, 0) + 1
        for k in nums2:
            d2[k] = d2.get(k, 0) + 1
        res = []
        nums2.sort()

        for v in set(nums1):
            i = 0
            j = len(nums2) - 1
            while i <= j:
                mid = (i + j) // 2
                if nums2[mid] == v:
                    res += [v for _ in range(min(d1[v], d2[v]))]
                    break
                elif nums2[mid] > v:
                    j = mid - 1
                else:
                    i = mid + 1
        return res