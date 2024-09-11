# source:https://leetcode.cn/problems/maximize-win-from-two-segments/description/ 二分+贪心
from typing import List

class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        # 二分查找右边界
        def findright(value):
            i = 0
            j = len(prizePositions)
            while i < j:
                mid = (i + j) // 2
                if prizePositions[mid] <= value:
                    i = mid + 1
                else:
                    j = mid
            return i
        
        # 二分查找左边界
        def findleft(value):
            i = 0
            j = len(prizePositions)
            while i < j:
                mid = (i + j) // 2
                if prizePositions[mid] < value:
                    i = mid + 1
                else:
                    j = mid
            return i
        
        n = len(prizePositions)
        # 用于记录在 prizePositions 的某个位置能获取的奖品数
        max_left = [0] * (n + 1)
        res = 0
        
        # 处理左到右线段
        for i in range(n):
            left = findleft(prizePositions[i] - k)
            max_left[i + 1] = max(max_left[i], i - left + 1)
        
        # 右到左扫描，计算两段组合的最大奖品数
        for i in range(n):
            right = findright(prizePositions[i] + k)
            res = max(res, (right - i) + max_left[i])
        
        return res

# source:https://leetcode.cn/problems/island-perimeter/description/
from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def bfs(i, j):
            count = 0
            q = deque()
            q.append([i, j])
            visit[i][j] = 1
            while q:
                x, y = q.popleft()
                temp = 4
                for m, n in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                    new_x = x + m
                    new_y = y + n
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                        if grid[new_x][new_y] == 1:
                            temp -= 1
                            if not visit[new_x][new_y]:
                                visit[new_x][new_y] = 1
                                q.append([new_x, new_y])
                
                count += temp
            return count
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return bfs(i,j)