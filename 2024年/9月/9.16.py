# source:https://leetcode.cn/problems/maximum-number-of-moves-in-a-grid/ 注意剪枝

from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if memo[i][j] != -1:
                return memo[i][j]
            
            max_move = 0
            for m, n in [[1,1],[0,1],[-1,1]]:
                x = m + i
                y = n + j
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] > grid[i][j]:
                    max_move = max(max_move, dfs(x, y))
                     
            memo[i][j] = max_move + 1
            return memo[i][j]

        rows, cols = len(grid), len(grid[0])
        memo = [[-1 for _ in range(cols)] for _ in range(rows)]
        result = 0

        for i in range(rows):
            result = max(result, dfs(i, 0))

        return result - 1
