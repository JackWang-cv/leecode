# source:https://leetcode.cn/problems/bus-routes/description/ bfs
from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop_to_bus = defaultdict(list)
        for i, route in enumerate(routes):
            for v in route:
                stop_to_bus[v].append(i)
        
        if source not in stop_to_bus.keys() or target not in stop_to_bus.keys():
            return -1 if source != target else 0
        
        d = {source:0}
        q = deque()
        q.append(source)
        while q:
            x = q.popleft()
            for v in stop_to_bus[x]:
                if routes[v]:
                    for i in routes[v]:
                        if i not in d.keys():
                            d[i] = d[x] + 1
                            q.append(i)
                    routes[v] = None
        return d.get(target, -1)

# source:https://leetcode.cn/problems/number-of-closed-islands/description/
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        def bfs(i, j, flag):
            q.append([i, j])
            while q:
                x, y = q.popleft()
                grid[x][y] = -1
                if flag and not (0 < x < len(grid)-1 and 0 < y < len(grid[0])-1):
                    flag = False
                for m, n in [[1,0],[0,-1],[-1,0],[0,1]]:
                    new_x = x + m
                    new_y = y + n
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                        if grid[new_x][new_y] != -1 and not grid[new_x][new_y]:
                            q.append([new_x, new_y])
                            
            return flag                                

        q = deque()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != -1 and not grid[i][j]:
                    if bfs(i, j, True):
                        count += 1
        return count
