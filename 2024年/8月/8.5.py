# source:https://leetcode.cn/problems/maximum-erasure-value/description/ 滑窗
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        mx = count = 0
        i = j = 0
        record = []
        while j < len(nums):
            while nums[j] in record:
                count -= nums[i]
                record.remove(nums[i])
                i += 1
            count += nums[j]
            record.append(nums[j])
            j += 1
            mx = max(mx, count)
        return mx

# source:https://leetcode.cn/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/ 定长滑窗
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = count = add = i = 0
        for v in arr:
            add += v
            count += 1
            if count >= k:
                if count != k:
                    add -= arr[i]
                    i += 1
                # print(add)
                res += 1 if add / k >= threshold else 0
        return res

# source:https://leetcode.cn/problems/length-of-longest-subarray-with-at-most-k-frequency/description/
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i = j = 0
        mx = 0
        dit = {}
        while j < len(nums):
            dit[nums[j]] = dit.get(nums[j], 0) + 1
            while dit.get(nums[j], 0) > k:
                dit[nums[i]] -= 1
                i += 1
            mx = max(mx, j - i + 1)
            j += 1
        return mx