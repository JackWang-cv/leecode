# source:https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-i/ 字典树+搜索
class Node():
    def __init__(self):
        self.son = {}
        self.end = False

class Tree:
    def __init__(self):
        self.root = Node()
    def add(self, words):
        cur = self.root
        for c in words:
            if c not in cur.son.keys():
                cur.son[c] = Node()
            cur = cur.son[c]
        cur.end = True

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        tr = Tree()
        for word in words:
            tr.add(word)
        
        @cache
        def dfs(i):
            if i >= n:
                return 0
            ans = inf
            cur = tr.root
            for j in range(i, n):
                if target[j] not in cur.son.keys():
                    break
                ans = min(ans, 1+dfs(j+1))
                cur = cur.son[target[j]]
            return ans

        n = len(target)
        ans = dfs(0)
        return ans if ans < inf else -1

# source:https://www.lanqiao.cn/problems/2094/learning/?page=1&first_category_id=1&problem_id=2094 并查集+搜索
import os
import sys

# 请在此输入您的代码
def find(x: int):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x: int, y: int):
    x_root = find(x)
    y_root = find(y)
    if x_root == y_root:
        return False
    parent[x_root] = y_root
    return True

def dfs(i: int, j: int):
  flag[i] = False
  total[i] = j
  for child, dis in g[i]:
    if flag[child]:
      dfs(child, j + dis)


n, m, q = list(map(int, input().split()))
parent = [i for i in range(n + 1)]
g = [[] for _ in range(n + 1)]  # 建图

for _ in range(m):
    l, r, s = list(map(int, input().split()))
    l = l - 1  # key
    flag = union(l, r)
    if flag:   # 这样就不会构造出环
        g[l].append([r, s])
        g[r].append([l, -s])
    
total = [0] * (n + 1)
flag = [True] * (n + 1)
for i in range(n + 1):
  if flag[i]:  # 表示当前的 节点 i 没有访问过
    dfs(i, 0)

for _ in range(q):
    l, r = list(map(int, input().split()))
    l = l - 1
    if find(l) != find(r):
        print('UNKNOWN')
    else:
        print(total[r] - total[l])