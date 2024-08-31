# source:https://leetcode.cn/problems/make-a-square-with-the-same-color/description/
from ast import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        zb = [[0,0],[0,1],[1,0],[1,1]]
        offset = [[0,1],[1,0],[1,1]]
        for i, j in zb:
            count = 1
            ori = grid[i][j]
            for m, n in offset:
                if grid[i+m][j+n] == ori:
                    count += 1
            if count != 2:
                return True
        return False
