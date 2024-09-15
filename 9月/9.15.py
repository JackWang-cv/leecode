# source:https://leetcode.cn/problems/points-that-intersect-with-cars/description/
from collections import deque
from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        stack = []
        nums.sort(key=lambda x:x[0])
        for i, j in nums:
            while stack:
                m, n = stack[-1]
                if (i <= m and j >= m) or (m <= i <= n):
                    i = min(i, m)
                    j = max(j, n)
                    stack.pop()
                else:
                    break
            stack.append([i, j])
        left = stack[0][0] - 1
        for i in range(1,len(stack),1):
            left += stack[i][0] - stack[i-1][1] - 1
        
        return stack[-1][-1] - left

# source:https://leetcode.cn/problems/number-of-enclaves/
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        visit = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def bfs(i, j, count):
            q = deque()
            q.append([i, j])
            visit[i][j] = 1
            flag = False if 0 == i or len(grid)-1 == i or 0 == j or len(grid[0])-1 == j else True
            while q:
                x, y = q.popleft()
                count += 1
                for m, n in [[1,0],[0,-1],[-1,0],[0,1]]:
                    new_x = x + m
                    new_y = y + n
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                        if not visit[new_x][new_y] and grid[new_x][new_y] == 1:
                            if 0 == new_x or len(grid)-1 == new_x or 0 == new_y or len(grid[0])-1 == new_y:
                                flag = False
                            q.append([new_x, new_y])
                            visit[new_x][new_y] = 1
            return count if flag else 0
                

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visit[i][j]:
                    count += bfs(i, j, 0)
        return count