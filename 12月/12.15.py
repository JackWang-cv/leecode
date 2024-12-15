# source:https://leetcode.cn/problems/reduce-array-size-to-the-half/ 贪心
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = defaultdict(int)
        for v in arr:
            d[v] += 1
        x = sorted(d.items(), key=lambda x:-x[1])
        # print(x)
        res = 0
        for index, (i, j) in enumerate(x):
            res += j
            if res >= len(arr)//2:
                return index+1

# source:https://leetcode.cn/problems/redundant-connection/ 并查集
class Union:
    def __init__(self, n):
        self.f = list(range(n))
    def find(self, x):
        if x == self.f[x]:
            return x
        else:
            self.f[x] = self.find(self.f[x])
            return self.f[x]
    def union(self, x, y):
        ori1 = self.f[x]
        ori2 = self.f[y]
        self.f[ori1] = ori2

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = Union(len(edges))
        for i, j in edges:
            if uf.find(i-1) != uf.find(j-1):
                uf.union(i-1, j-1)
            else:
                ans = [i, j]
        return ans

# source:
class Union:
    def __init__(self, n):
        self.f = list(range(n))
    def find(self, x):
        if x == self.f[x]:
            return x
        else:
            self.f[x] = self.find(self.f[x])
            return self.f[x]
    def union(self, x, y):
        ori1 = self.f[x]
        ori2 = self.f[y]
        self.f[ori2] = ori1

# source:https://leetcode.cn/problems/redundant-connection-ii/ 上一题的升级版，加多了限制条件，需要具体分析
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        uf = Union(len(edges))
        cycle, conflict = -1, -1
        parent = list(range(len(edges)+1))
        for index, (i, j) in enumerate(edges):
            if parent[j] != j:
                conflict = index
            else:
                parent[j] = i
                if uf.find(i-1) != uf.find(j-1):
                    uf.union(i-1, j-1)
                else:
                    cycle = index
        if conflict < 0:
            return [edges[cycle][0], edges[cycle][1]]
        else:
            conflictEdge = edges[conflict]
            if cycle >= 0:
                return [parent[conflictEdge[1]], conflictEdge[1]]
            else:
                return [conflictEdge[0], conflictEdge[1]]