# source:https://leetcode.cn/problems/squares-of-a-sorted-array/description/ 双指针
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        seg = len(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                seg = i
                break
        res = []
        if seg == len(nums):
            for i in range(len(nums)-1, -1, -1):
                res.append(pow(nums[i], 2))
        elif seg == 0:
            for i in range(len(nums)):
                res.append(pow(nums[i], 2))
        else:
            m = seg -1
            n = seg
            for i in range(len(nums)):
                if m >= 0:
                    t1 = nums[m]
                else:
                    res.append(pow(nums[n], 2))
                    n += 1
                    continue

                if n <= len(nums)-1:
                    t2 = nums[n]
                else:
                    res.append(pow(nums[m], 2))
                    m -= 1
                    continue

                if abs(t1) < abs(t2):
                    res.append(pow(t1, 2))
                    m -= 1
                else:
                    res.append(pow(t2, 2))
                    n += 1
        return res

# source:https://leetcode.cn/problems/max-area-of-island/description/ bfs
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(i, j)->int:
            visit[i][j] = 1
            q.append([i, j])
            t = 1
            while q:
                x, y = q.popleft()
                for m, n in [[0,1],[1,0],[0,-1],[-1,0]]:
                    new_x = x + m
                    new_n = y + n
                    if 0 <= new_x <= len(grid)-1 and 0 <= new_n <= len(grid[0])-1:
                        if not visit[new_x][new_n] and grid[new_x][new_n]:
                            q.append([new_x, new_n])
                            t += 1
                            visit[new_x][new_n] = 1
            return t
        
        q = deque()
        count = 0
        visit = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visit[i][j] and grid[i][j]:
                    count = max(count, bfs(i, j))
        return count