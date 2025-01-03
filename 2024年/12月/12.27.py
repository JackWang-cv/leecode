# source:https://leetcode.cn/submissions/detail/589672115/ 二分

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def judge(value):
            cnt = 0
            for v in nums:
                if v > value:
                    cnt += v//value-1 if v % value == 0 else v//value 
            # print(value, cnt)
            return cnt > maxOperations
        
        i, j = 1, max(nums)
        while i < j:
            mid = (i+j) // 2
            if judge(mid):
                i = mid+1
            else:
                j = mid
        return i

# source:https://leetcode.cn/problems/path-with-minimum-effort/ 二分+ BFS
from collections import deque
from typing import List
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        mx = 0
        q = deque()
        row, col = len(heights), len(heights[0])
        direction = [[1,0],[0,-1],[-1,0],[0,1]]
        for i in range(row):
            for j in range(col):
                mx = max(mx, heights[i][j])
        
        def find(value):
            # BFS
            q.clear()
            q.append([0, 0])
            visited = [[0 for _ in range(col)] for _ in range(row)]
            visited[0][0] = 1
            while q:
                x, y = q.popleft()
                # print(x, y)
                if x == row-1 and y == col-1:
                    return False
                for i, j in direction:
                    new_x = x + i
                    new_y = y + j
                    if 0 <= new_x < row and 0 <= new_y < col and not visited[new_x][new_y] and abs(heights[new_x][new_y] - heights[x][y]) <= value:
                        q.append([new_x, new_y])
                        visited[new_x][new_y] = 1
            return True

        i, j = 0, mx
        while i < j:
            mid = (i+j)//2
            if find(mid):
                i = mid+1
            else:
                j = mid
        return i
    
# 法二：并查集模板
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n
    
    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]
    
    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True
    
    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        edges = list()
        for i in range(m):
            for j in range(n):
                iden = i * n + j
                if i > 0:
                    edges.append((iden - n, iden, abs(heights[i][j] - heights[i - 1][j])))
                if j > 0:
                    edges.append((iden - 1, iden, abs(heights[i][j] - heights[i][j - 1])))
        
        edges.sort(key=lambda e: e[2])

        uf = UnionFind(m * n)
        ans = 0
        for x, y, v in edges:
            uf.unite(x, y)
            if uf.connected(0, m * n - 1):
                ans = v
                break
        
        return ans