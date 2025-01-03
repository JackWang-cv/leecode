# source:https://leetcode.cn/problems/knight-probability-in-chessboard/ dfs 记忆化搜索
from functools import cache


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache
        def dfs(x, y, prob, cnt):
            if cnt == k:
                return prob
            ans = 0
            for i, j in direction:
                new_i = i + x
                new_j = j + y
                if 0 <= new_i < n and 0 <= new_j < n:
                    ans += dfs(new_i, new_j, prob*1/8, cnt+1)
            return ans
        
        direction = [[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2]]
        return dfs(row, column, 1, 0)

# source:https://leetcode.cn/problems/sum-of-prefix-scores-of-strings/description/ 字典树
from typing import List

class Node:
    def __init__(self):
        self.son = {}
        self.count = 0  # 表示到达该节点的路径数量（即前缀数目）

class Solution:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        cur = self.root
        for c in word:
            if c not in cur.son:
                cur.son[c] = Node()
            cur = cur.son[c]
            cur.count += 1  # 每次经过一个节点，更新路径数量

    def query(self, word):
        cur = self.root
        total_score = 0
        for c in word:
            cur = cur.son[c]
            total_score += cur.count  # 累加当前节点的前缀计数
        return total_score

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        for word in words:  # 构建字典树
            self.add(word)

        results = []
        for word in words:  # 查询每个单词的前缀分数和
            results.append(self.query(word))
        
        return results
