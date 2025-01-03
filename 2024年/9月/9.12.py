# source:https://leetcode.cn/problems/insert-interval/ 栈
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        res = []
        flag = False
        for v, (i, j) in enumerate(intervals):
            if (newInterval[0] <= i and newInterval[1] >= i) or (i <= newInterval[0] <= j):
                intervals[v] = [min(i, newInterval[0]), max(newInterval[1], j)]
                flag = True
                break
        if not flag:
            intervals.append(newInterval)
        intervals.sort(key = lambda x:x[0])
        for v, (i, j) in enumerate(intervals):
            if not res:
                res.append(intervals[v])
            else:
                while res:
                    left = res[-1][0]
                    right = res[-1][1]
                    if (i <= left and j >= left) or (left <= i <= right):
                        res.pop()
                        i = min(left, i)
                        j = max(right, j)
                    else:
                        break
                res.append([i, j])
        return res

# source:https://leetcode.cn/problems/maximum-number-of-fish-in-a-grid/description/
from collections import deque
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        visit = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def bfs(i, j):
            q = deque()
            q.append([i, j])
            visit[i][j] = 1
            count = 0
            while q:
                x, y = q.popleft()
                count += grid[x][y]
                for m, n in [[1,0], [0,-1], [-1,0],[0,1]]:
                    new_x = x + m
                    new_y = y + n
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                        if not visit[new_x][new_y] and grid[new_x][new_y]>0:
                            q.append([new_x, new_y])
                            visit[new_x][new_y] = 1
            return count
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visit[i][j] and grid[i][j] > 0:
                    ans = max(ans, bfs(i, j))
        return ans