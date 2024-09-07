# source:https://leetcode.cn/problems/simplify-path/description/
from typing import List


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        s = path.split('/')
        for v in s:
            if v == '' or v == '.':
                continue
            if v == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(v)
        ans = ''
        for v in stack:
            ans += '/'
            ans += v
        return ans if ans else '/'
    

# source:https://leetcode.cn/problems/set-matrix-zeroes/description/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left = []
        right = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    left.append(i)
                    right.append(j)
 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i in left) or (j in right):
                    matrix[i][j] = 0

# source:https://leetcode.cn/problems/remove-k-digits/description/
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)-k == 0:
            return '0'
        stack = []
        temp = k
        for v in num:
            while stack and stack[-1] > v and temp > 0:
                stack.pop()
                temp -= 1
            stack.append(v)  
        ans = ''.join(stack) if len(stack) + k == len(num) else ''.join(stack[:len(num)-k])
        for i in range(len(ans)):
            if stack[i] != '0':
                return ans[i:]
        return '0'

# source:https://leetcode.cn/problems/number-of-islands/description/
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        q = deque()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visit[i][j] and grid[i][j] == '1':
                    visit[i][j] = 1
                    count += 1
                    q.append([i, j])
                    while q:
                        ii, jj = q.popleft()
                        for m, n in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                            new_i = ii + m
                            new_j = jj + n
                            if 0 <= new_i <= len(grid)-1 and 0 <= new_j <= len(grid[0])-1:
                                if grid[new_i][new_j] == '1' and not visit[new_i][new_j]:
                                    q.append([new_i, new_j])
                                    visit[new_i][new_j] = 1
        return count