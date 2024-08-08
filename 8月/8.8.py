# source: https://leetcode.cn/problems/find-the-integer-added-to-array-ii/description/ 排序+二分+贪心
from cmath import inf
from typing import List


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        def check(v, j):
            i = 0
            while i < j:
                mid = (i+j+1)//2
                if nums1[mid] <= v:
                    i = mid
                else:
                    j = mid-1
            return i
        
        nums1.sort()
        nums2.sort()
        res = inf
        for i in range(len(nums1)-1, len(nums2)-2, -1):
            flag = True
            lastv = inf
            right = len(nums1) - 2
            for j in range(len(nums2)-1, -1, -1):
                if lastv == inf:
                    lastv = nums2[j] - nums1[i]
                else: 
                    right = check(nums2[j] - lastv, right)
                    if nums1[right] == nums2[j] - lastv:
                        right -= 1
                    else:
                        flag = False
                        break
            if flag:
                return lastv

# source: https://leetcode.cn/problems/count-subarrays-with-score-less-than-k/description/ 滑动窗口
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        i = j = 0
        t = 0
        while j < len(nums):
            t += nums[j]
            while t * (j - i + 1) >= k:
                t -= nums[i]
                i += 1
            res += j - i + 1
            j += 1
        return res