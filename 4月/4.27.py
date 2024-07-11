# source: https://leetcode.cn/problems/find-the-width-of-columns-of-a-grid/
class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        res = []
        n = len(grid[0])
        for i in range(n):
            mx = 0
            for t in grid:
                if len(str(t[i])) > mx:
                    mx = len(str(t[i]))
            res.append(mx)
        return res