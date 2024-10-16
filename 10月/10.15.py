# source:https://leetcode.cn/problems/minimize-malware-spread/description/
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        visit = [0 for _ in range(len(graph))]
        count = [0 for _ in range(len(graph))]
        mn = inf
        ans = -1
        dit = defaultdict(list)
        for i, g in enumerate(graph):
            for j, v in enumerate(g):
                if v:
                    dit[i].append(j)

        def dfs(node):
            sign = 0
            if count[node]:
                return count[node]+1
            if not dit[node]:
                return 1
            for v in dit[node]:
                if not visit[v]:
                    visit[v] = 1
                    sign += dfs(v)
            count[node] = sign+1
            return sign
        
        for i in range(len(initial)):
            for _, j in enumerate(initial):
                if initial[i] != j and not visit[j]:
                    visit[j] = 1
                    dfs(j)
            if mn > sum(count):
                mn = sum(count)
                ans = initial[i]
            elif mn == sum(count):
                ans = min(ans, initial[i])
            for index in range(len(graph)):
                visit[index] = 0
                count[index] = 0       
        return ans

# source:
