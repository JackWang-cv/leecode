# source:https://leetcode.cn/problems/permutations/description/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visit = [0,] * len(nums)
        def find(value):
            temp.append(value)
            if len(temp) == len(nums):
                res.append(temp.copy())
                return
            for i, v in enumerate(nums):
                if not visit[i]:
                    visit[i] = 1
                    find(v)
                    temp.pop()
                    visit[i] = 0
        for j, k in enumerate(nums):
            visit = [0,] * len(nums)
            visit[j] = 1
            temp = []
            find(k)
        return res