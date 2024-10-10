# source:https://leetcode.cn/problems/find-the-number-of-good-pairs-ii/ 二分
from typing import Counter, List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count = 0
        nums1.sort()
        dit = Counter(nums1)
        dit_div = Counter(nums2)
        def find(v):
            i = 0
            j = len(nums1)-1
            while i <= j:
                mid = (i+j)//2
                if nums1[mid] == v:
                    return 1
                elif nums1[mid] > v:
                    j = mid-1
                else:
                    i = mid+1
            return 0
        for v in dit_div.keys():
            key = v * k
            i = 1
            while key * i <= nums1[-1]:
                if find(key * i):
                    count += dit[key*i]*dit_div[v]
                i += 1
        return count