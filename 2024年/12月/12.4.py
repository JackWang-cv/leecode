# source:https://leetcode.cn/problems/number-of-valid-move-combinations-on-chessboard/ dfs 逻辑
from typing import List, Tuple


class Solution:
    # 判断两个移动是否合法，即不存在同一时刻两个棋子重叠的情况
    def is_valid(self, move1: Tuple[int, int, int, int, int], move2: Tuple[int, int, int, int, int]) -> bool:
        x1, y1, dx1, dy1, step1 = move1
        x2, y2, dx2, dy2, step2 = move2
        for i in range(max(step1, step2)):
            # 每一秒走一步
            if i < step1:
                x1 += dx1
                y1 += dy1
            if i < step2:
                x2 += dx2
                y2 += dy2
            if x1 == x2 and y1 == y2:  # 重叠
                return False
        return True

    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        way1 = [[1,0],[0,-1],[-1,0],[0,1]]
        way2 = [[1,1],[1,-1],[-1,-1],[-1,1]]
        store = {"rook":way1, "queen":way1+way2, "bishop":way2}
        all_moves = []
        for i, x in enumerate(pieces):
            left = positions[i][0]
            right = positions[i][1]
            # d[(left, right)] = 1
            temp = [(left, right, 0, 0, 0)]
            for m, n in store[x]:
                new_left = left+m
                new_right = right+n
                step = 1
                while 0 < new_left <= 8 and 0 < new_right <= 8:
                    # d[(new_left,new_right)] += 1
                    temp.append((left, right, m, n, step))
                    new_left += m
                    new_right += n
                    step += 1
            all_moves.append(temp.copy())
        # print(temp)
        n = len(pieces)
        path = [None] * n  # 注意 path 的长度是固定的
        ans = 0
        def dfs(i: int) -> None:
            if i == n:
                nonlocal ans
                ans += 1
                return
            # 枚举当前棋子的所有合法移动
            for move1 in all_moves[i]:
                # 判断合法移动 move1 是否有效
                if all(self.is_valid(move1, move2) for move2 in path[:i]):
                    path[i] = move1  # 直接覆盖，无需恢复现场
                    dfs(i + 1)  # 枚举后续棋子的所有合法移动组合
        dfs(0)
        return ans

# source:https://leetcode.cn/problems/longest-word-in-dictionary/submissions/585068643/ 
class Node:
    def __init__(self):
        self.son = {}
        self.end = False

class Solution:
    def __init__(self):
        self.root = Node()
    def insert(self, word):
        cur = self.root
        for s in word:
            if s not in cur.son.keys():
                cur.son[s] = Node()
            cur = cur.son[s]
        cur.end = True

    def longestWord(self, words: List[str]) -> str:
        cur = self.root
        for w in words:
            self.insert(w)
        ans = ''
        mx = 0
        def dfs(temp, cur, cnt):
            nonlocal ans, mx
            if cur.son == {}:
                if mx < cnt:
                    mx = cnt
                    ans = temp
                return 
            
            for c in sorted(cur.son.keys()):
                if cur.son[c].end:
                    dfs(temp+c, cur.son[c], cnt + 1)
            else:
                if mx < cnt:
                    mx = cnt
                    ans = temp

        dfs('', cur, 0)
        return ans