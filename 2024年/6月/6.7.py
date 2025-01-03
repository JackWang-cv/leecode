# source:https://leetcode.cn/problems/maximum-number-of-operations-with-the-same-score-i/
from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        count = 1
        i = 2
        res = nums[0 ] +nums[1]
        while i< len(nums) - 1:

            if nums[i] + nums[i + 1] == res:
                count += 1
                i += 2
            else:
                break
        return count
