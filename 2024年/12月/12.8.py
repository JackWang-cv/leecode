# source:https://leetcode.cn/problems/unique-paths-ii/submissions/585783499/ dfs dp
class Solution:
    def __init__(self):
        self.ans = 0
        self.row, self.col = 0, 0 
        self.direction = [[1,0],[0,1]]
        self.dict = defaultdict(int)

    def dfs(self, i, j):
        if i == self.row-1 and j == self.col-1 and not self.store[i][j]:
            self.dict[(i, j)] = 1
            return 1
        if self.dict[(i, j)]:
            return self.dict[(i, j)]
        cur = 0
        for m, n in self.direction:
            x = i + m
            y = j + n
            if 0 <= x < self.row and 0 <= y < self.col and not self.store[x][y]:
                cur += self.dfs(x, y)
        self.dict[(i, j)] = cur
        return self.dict[(i, j)]
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ans = 0
        self.row = len(obstacleGrid)
        self.col = len(obstacleGrid[0])
        self.store = obstacleGrid
        return self.dfs(0, 0) if not self.store[0][0] else 0
# 法二：dp
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        f = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    if not obstacleGrid[i][j]:
                        f[i+1][j+1] = 1
                    else:
                        f[i+1][j+1] = 0
                else:
                    if obstacleGrid[i][j] == 1:
                        f[i+1][j+1] = 0
                    else:
                        f[i+1][j+1] = f[i][j+1] + f[i+1][j]
        return f[-1][-1]

# source:https://leetcode.cn/problems/satisfiability-of-equality-equations/ 并查集
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if x == d[x]:
                return x
            else:
                d[x] = find(d[x])
                return d[x]

        def union(i, j):
            ori1 = find(i)
            ori2 = find(j)
            d[ori1] = ori2
        
        red = []
        d = defaultdict(int)
        for s in equations:
            i, j = s[0], s[-1]
            d[i] = i
            d[j] = j
        for s in equations:
            if s[1] == '!':
                red.append(s)
                continue
            union(s[0], s[-1])
        for s in red:
            if find(s[0]) == find(s[-1]):
                return False
        return True