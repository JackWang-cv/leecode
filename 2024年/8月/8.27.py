#source:https://leetcode.cn/problems/combination-sum-ii/description/
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # 先排序
        res = []
        
        def dfs(total, index, path):
            if total == target:
                res.append(path)
                return
            if total > target:
                return
            
            for i in range(index, len(candidates)):
                # 如果当前元素和前一个元素相同，且前一个元素没有被使用，则跳过
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                # 进行下一步的递归
                dfs(total + candidates[i], i + 1, path + [candidates[i]])
        
        dfs(0, 0, [])
        return res
