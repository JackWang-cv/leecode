# source:https://leetcode.cn/problems/maximum-number-of-operations-with-the-same-score-ii/description/ dfs
from typing import List


class Solution:

    def maxOperations(self, nums: List[int]) -> int:
        t1 = nums[0 ] +nums[1]
        t2 = nums[-2 ] +nums[-1]
        t3 = nums[0 ] +nums[-1]
        k = [t1, t2, t3]
        res = 0

        def find(nums, l, r, k):
            if l>= r:
                return 0
            ans = 0
            if nums[l] + nums[l + 1] == k:
                ans = max(ans, 1 + find(nums, l + 2, r, k))
            if nums[l] + nums[r] == k:
                ans = max(ans, find(nums, l + 1, r - 1, k) + 1)
            if nums[r] + nums[r - 1] == k:
                ans = max(ans, 1 + find(nums, l, r - 2, k))
            return ans

        for i in range(3):
            res = max(res, find(nums, 0, len(nums) - 1, k[i]))

        return res
