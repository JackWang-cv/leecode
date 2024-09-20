# source:https://leetcode.cn/problems/check-if-there-is-a-valid-path-in-a-grid/description/ dfs 
from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        d = {1:[[0,-1],[0,1]], 2:[[-1,0],[1,0]], 3:[[0,-1],[1,0]], 4:[[0,1],[1,0]], 5:[[0,-1],[-1,0]], 6:[[0,1],[-1,0]]}
        visit = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def dfs(i, j):
            if i == len(grid)-1 and j == len(grid[0])-1:
                return True
            
            flag = False
            for m, n in d[grid[i][j]]:
                new_x = i + m
                new_y = j + n
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                    if not visit[new_x][new_y]:
                        for x, y in d[grid[new_x][new_y]]:
                            if x + m == 0 and y + n == 0:
                                break
                        else:
                            continue
                        visit[new_x][new_y] = 1
                        flag = flag or dfs(new_x, new_y)
                        visit[new_x][new_y] = 0
            return flag
        visit[0][0] = 1
        return dfs(0, 0)
    
# source:https://leetcode.cn/problems/subsets-ii/ dfs
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        visit = [-11 for _ in range(len(nums))]
        def dfs(temp, index):
            res.append(temp)
            for i in range(index, len(nums), 1):
                if visit[i] == -11:
                    if i > 0 and nums[i] == nums[i-1] and -11 == visit[i-1]:
                        continue
                    visit[i] = 11
                    dfs(temp + [nums[i]], i+1)
                    visit[i] = -11
        dfs([], 0)
        return res