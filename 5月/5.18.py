# source:https://leetcode.cn/problems/find-the-maximum-divisibility-score/ 
from typing import List


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        res = 0
        s = 0
        for i in divisors:
            score = 0
            for j in nums:
                if j % i == 0:
                    score += 1
            if score > s:
                s = score
                res = i
            elif s == score:
                if i < res:
                    res = i
        if res == 0:
            res = min(divisors)
        return res


m = Solution()
nums = [3,4,5,6]
divisors = [2,3]
print(m.maxDivScore(nums,divisors))