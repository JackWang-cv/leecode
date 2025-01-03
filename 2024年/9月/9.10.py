# source:https://leetcode.cn/problems/gray-code/
from typing import List

# 回溯会超时
# class Solution:
#     def grayCode(self, n: int) -> List[int]:
#         n = pow(2, n)
#         visit = [0 for _ in range(n)]
#         def dfs(temp):
#             if len(temp) == n:
#                 final = bin(temp[-1] ^ temp[0])[2:]
#                 if final.count('1') == 1:
#                     return temp
#             for i in range(0, n, 1):
#                 if not visit[i]:
#                     if not temp:
#                         visit[i] = 1
#                         res = dfs(temp + [i])
#                         if res:
#                             return res
#                         visit[i] = 0
#                     else:
#                         res = bin(i ^ temp[-1])[2:]
#                         if res.count('1') == 1:
#                             visit[i] = 1
#                             dfs(temp + [i])
#                             visit[i] = 0
#             return []
#         return dfs([])
# 找规律
class Solution1:
    def grayCode(self, n: int) -> List[int]:
        return [(i >> 1) ^ i for i in range(1 << n)]

# source:https://leetcode.cn/problems/YesdPw/description/
from collections import deque
class Solution:
    def largestArea(self, grid: List[str]) -> int:
        visit = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def bfs(i, j):
            nonlocal flag
            q = deque()
            q.append([i, j])
            visit[i][j] = 1
            count = 0
            while q:
                x, y = q.popleft()
                count += 1
                if grid[x][y] == '0' or x == 0 or x == len(grid)-1 or y == 0 or y == len(grid[0])-1:
                    flag = False
                for m, n in [[1,0],[0,-1],[-1,0],[0,1]]:
                    new_x = x + m
                    new_y = y + n
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                        if grid[new_x][new_y] == '0':
                            flag = False
                        if not visit[new_x][new_y] and grid[new_x][new_y] == grid[x][y]:
                            visit[new_x][new_y] = 1
                            q.append([new_x, new_y])
            return count if flag else -1
                
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visit[i][j]:
                    flag = True
                    ans = max(ans, bfs(i, j))
        return ans
