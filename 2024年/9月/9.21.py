# source:https://leetcode.cn/problems/node-with-highest-edge-score/description/ 哈希表，排序
from cmath import inf
from collections import defaultdict
from typing import List


class Solution1:
    def edgeScore(self, edges: List[int]) -> int:
        d = defaultdict(int)
        for i, v in enumerate(edges):
            d[v] += i
        ans = value = inf
        for i, j in sorted(d.items(), key=lambda x:x[1], reverse=True):
            if ans == inf :
                ans = i
                value = j
            elif value == j and ans > i:
                ans = i
            elif value > j:
                break
        return ans

# source:https://leetcode.cn/problems/pacific-atlantic-water-flow/description/ dfs
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        h = len(heights)
        w = len(heights[0])
        if min(h, w) == 1:
            res = []
            for i in range(h):
                for j in range(w):
                    res.append([i, j])
            return res
        
        visit = [[0 for _ in range(w)] for _ in range(h)]
        visit[0][w-1] = 2
        visit[h-1][0] = 2
        
        def dfs(i, j):
            nonlocal total, h, w, flag0, flag1
            if (i == 0 or j == 0) and flag0:
                total += 1
                flag0 = False
                if total == 2:
                    return True
            elif (i == h-1 or j == w-1) and flag1:
                total += 1
                flag1 = False
                if total == 2:
                    return True

            flag = False
            for m, n in [[1,0],[0,-1],[-1,0],[0,1]]:
                x = i + m
                y = j + n
                if 0 <= x < h and 0 <= y < w and heights[x][y] <= heights[i][j]:
                    if not visit[x][y]:
                        visit[x][y] = 1
                        flag = flag or dfs(x, y)
                        visit[x][y] = 0
                        if flag:
                            break
                    elif visit[x][y] == 2:
                        flag = True
                        break
            return flag

        
        res = [[0, w-1], [h-1, 0]]
        for i in range(h):
            for j in range(w):
                if not visit[i][j]:
                    visit[i][j] = 1
                    total = 0
                    flag0 = flag1 = True
                    if dfs(i, j):
                        visit[i][j] = 2
                        res.append([i, j])
                    else:
                        visit[i][j] = 0
        return res