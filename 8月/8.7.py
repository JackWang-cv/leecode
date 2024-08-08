# source:https://leetcode.cn/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/ 滑窗
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        i = j = 0
        count = 0
        cmx = 0
        mx = max(nums)
        while j<len(nums):
            if nums[j] == mx:
                cmx += 1
            while cmx == k:
                count += len(nums)-j
                if nums[i] == mx:
                    cmx -= 1
                i += 1
            j += 1
        return count

#source:https://leetcode.cn/problems/max-consecutive-ones-iii/description/ 滑窗
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = j = 0
        mx = count0 = 0
        while j < len(nums):
            if not nums[j]:
                count0 += 1
            while count0 == k+1:
                if not nums[i]:
                    count0 -= 1
                i += 1
            mx = max(mx, j - i + 1)
            j += 1
        return mx
                
