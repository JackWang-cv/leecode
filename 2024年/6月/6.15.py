# soource:https://leetcode.cn/problems/maximum-beauty-of-an-array-after-applying-operation/ 排序+差分
from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda nums: -nums)
        t = []
        for i in range(len(nums) - 1):
            t.append(nums[i] - nums[i + 1])

        s = 1
        mx = j = temp = 0

        for i in range(len(t)):
            temp += t[i]
            if temp <= 2 * k:
                s += 1
            else:
                temp -= t[j]
                j += 1
            mx = max(mx, s)
        mx = max(mx, s)
        return mx



