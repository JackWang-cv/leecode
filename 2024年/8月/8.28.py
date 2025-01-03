# source:https://leetcode.cn/problems/permutations-ii/
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visit = {}
        sign = [0 for _ in range(len(nums))]
        res = []
        def dfs(count, temp, last):
            if count == len(nums):
                res.append(temp)
            for i in range(len(nums)):
                if not sign[i]:
                    if temp[-1] == nums[i] and last + 1 != i:
                        continue
                    sign[i] = 1
                    dfs(count+1, temp+[nums[i]], i)
                    sign[i] = 0
        for i, v in enumerate(nums):
            if not visit.get(v, 0):
                visit[v] = 1
                sign[i] = 1
                dfs(1, [v], i)
                sign[i] = 0
        return res

X = Solution()
X.permuteUnique([1,1,2,2])