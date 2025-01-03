# source:https://leetcode.cn/problems/maximum-spending-after-buying-items/ 最小堆
from collections import defaultdict
import heapq
class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        row, col = len(values), len(values[0])
        # print(d)
        store = []
        for i in range(row):
            store.append((values[i][-1], i, 1))
        heapq.heapify(store)
        ans = 0
        for i in range(1, row*col+1):
            x, index, cnt = heapq.heappop(store)
            ans += i * x
            if cnt != col:
                heapq.heappush(store, (values[index][col-1-cnt], index, cnt+1))
        return ans

# source:https://leetcode.cn/problems/lexicographically-smallest-equivalent-string/ 并查集
class Union:
    def __init__(self):
        self.d = defaultdict(str)
        for i in range(26):
            self.d[chr(i+97)] = chr(i+97)
    def find(self, x):
        if x == self.d[x]:
            return x
        else:
            self.d[x] = self.find(self.d[x])
            return self.d[x]
    def union(self, x, y):
        ori1 = self.find(x)
        ori2 = self.find(y)
        if ori1 < ori2:
            self.d[ori2] = ori1
        else:
            self.d[ori1] = ori2
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = Union()
        for i in range(len(s1)):
            uf.union(s1[i], s2[i])
        # print(uf.d)
        ans = ''
        for v in baseStr:
            ans += uf.find(v)
        return ans

