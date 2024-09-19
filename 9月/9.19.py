# source:https://leetcode.cn/problems/count-sub-islands/description/
from collections import deque
from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i, j) -> bool:
            # 如果当前点已经访问过或者是水域，直接返回 True
            if i < 0 or i >= len(grid2) or j < 0 or j >= len(grid2[0]) or grid2[i][j] != 1:
                return True
            
            # 标记为访问过
            grid2[i][j] = -1
            
            # 如果 grid1 里这个位置不是陆地，flag 为 False，说明这块不能作为子岛
            flag = grid1[i][j] == 1
            
            # 遍历上下左右四个方向
            for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                flag &= dfs(i + dx, j + dy)

            return flag
        
        count = 0
        
        # 遍历 grid2 找到所有未访问的岛屿
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    # 如果这个岛屿是子岛，计数加一
                    if dfs(i, j):
                        count += 1
        
        return count
