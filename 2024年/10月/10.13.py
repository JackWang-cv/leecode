# source:
from collections import defaultdict, deque
from typing import List


class Solution1:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dit = defaultdict(list)
        for i, j in edges:
            dit[i].append(j)
            dit[j].append(i)
        visit = [0 for _ in range(n)]
        def bfs(node):
            q = deque()
            q.append(node)
            flag = False
            while q:
                x = q.popleft()
                visit[x] = 1
                if x == destination:
                    flag = True
                for value in dit[x]:
                    if not visit[value]:
                        q.append(value)
            return flag
        return bfs(source) 

# source:https://leetcode.cn/problems/all-paths-from-source-to-target/description dfs
class Solution2:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(graph)
        visit = [0 for _ in range(n)]
        
        def dfs(node_list):
            if node_list[-1] == n-1:
                ans.append(node_list)
                return 
            for v in graph[node_list[-1]]:
                if not visit[v]:
                    visit[v] = 1
                    dfs(node_list + [v])
                    visit[v] = 0
        visit[0] = 1
        dfs([0])
        return ans   

# source:https://leetcode.cn/problems/keys-and-rooms/description/ bfs
class Solution3:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        admit = defaultdict(int)
        admit[0] = 1
        q = deque()
        q.append(0)
        while q:
            v = q.popleft()
            for node in rooms[v]:
                if admit[node] == 0:
                    admit[node] = 1
                    q.append(node)
        
        return len(admit) == len(rooms)   

# source:https://leetcode.cn/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/ dfs
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        dit = defaultdict(list)
        for i, j in edges:
            dit[i].append(j)
            dit[j].append(i)
        visit = [0 for _ in range(n)]
        def dfs(node):
            ctr = 0
            for v in dit[node]:
                if not visit[v]:
                    visit[v] = 1
                    ctr += dfs(v)
            return ctr+1
        
        ans = total = 0
        for i in range(n):
            if not visit[i]:
                visit[i] = 1
                size = dfs(i)
                ans += size*total
                total += size
        return ans
            
