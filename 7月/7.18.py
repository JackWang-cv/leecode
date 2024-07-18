# source:https://leetcode.cn/problems/minimum-time-to-visit-disappearing-nodes/description/
# 迪杰斯特拉这种问题会超时 复杂度O(n^2)
# from typing import List

# class Solution:
#     def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
#         inf = float('inf')
#         matrix = [[inf for _ in range(n)] for _ in range(n)]

#         for i, j, k in edges:
#             matrix[i][j] = min(matrix[i][j], k)
#             matrix[j][i] = min(matrix[j][i], k)

#         visit = [0 for _ in range(n)]
#         dist = [0] + [inf for _ in range(n - 1)]

#         while True:
#             mn = inf
#             t = -1
#             for i in range(n):
#                 if not visit[i] and mn > dist[i]:
#                     mn = dist[i]
#                     t = i

#             if t == -1:
#                 break

#             visit[t] = 1
#             for j in range(n):
#                 if matrix[t][j] != inf and not visit[j]:
#                     if mn + matrix[t][j] < dist[j] and mn + matrix[t][j] < disappear[j]:
#                         dist[j] = mn + matrix[t][j]

#         for i in range(n):
#             if dist[i] == inf or dist[i] >= disappear[i]:
#                 dist[i] = -1

#         return dist

# 在稀疏图中，松弛操作远小于n，所以考虑在此进行优化。
# 1.将最短距离出队。优化的关键是省去对dist的线性查找，如果每次可以直接返回dist中的最小值，就可以大大减小算法的时间复杂度。
# 2.进行松弛操作，并将成功松弛的点入队。
# 使用邻接表和堆加速 复杂度O(n + mlogm), n为顶点数, m为边数

from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        inf = float('inf')
        graph = [[] for _ in range(n)]

        for u, v, length in edges:
            graph[u].append((v, length))
            graph[v].append((u, length))

        dist = [inf] * n
        dist[0] = 0
        pq = [(0, 0)]  # (distance, node)

        while pq:
            curr_dist, u = heappop(pq)

            if curr_dist >= disappear[u]:
                continue

            if curr_dist > dist[u]:
                continue

            for v, length in graph[u]:
                if curr_dist + length < dist[v] and curr_dist + length < disappear[v]:
                    dist[v] = curr_dist + length
                    heappush(pq, (dist[v], v))

        for i in range(n):
            if dist[i] == inf or dist[i] >= disappear[i]:
                dist[i] = -1

        return dist