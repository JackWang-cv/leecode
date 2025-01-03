# source:https://leetcode.cn/problems/maximum-height-of-a-triangle/ 枚举
from cmath import inf
from typing import List


class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def find(top, second):
            count = 0
            while top >= count+1 and second >= count+2:
                top -= count+1
                second -= count+2
                count += 2
            if top >= count+1:
                count += 1
            return count
        ans = 0
        ans = max(ans, find(red, blue))
        ans = max(ans, find(blue, red))
        return ans

# source:https://leetcode.cn/problems/minimum-score-of-a-path-between-two-cities/description/
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y, d in roads:
            g[x - 1].append((y - 1, d))
            g[y - 1].append((x - 1, d))
        ans = inf
        vis = [False] * n
        def dfs(x: int) -> None:
            nonlocal ans
            vis[x] = True
            for y, d in g[x]:
                ans = min(ans, d)
                if not vis[y]:
                    dfs(y)
        dfs(0)
        return ans

