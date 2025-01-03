# source:https://leetcode.cn/submissions/detail/585390471/ 字典树
class Node:
    def __init__(self):
        self.son = {}
        self.end = False

class Solution:
    def __init__(self):
        self.root = Node()
        self.ans = 0
    def add(self, word):
        cur = self.root
        for c in word[::-1]:
            if c not in cur.son.keys():
                cur.son[c] = Node()
            cur = cur.son[c]
        cur.end = True

    def dfs(self, node, cnt):
        if not node.son:
            self.ans += cnt + 1
            return 
        for v in node.son.keys():
            self.dfs(node.son[v], cnt+1)
        
    def minimumLengthEncoding(self, words: List[str]) -> int:
        for v in words:
            self.add(v)
        self.dfs(self.root, 0)
        return self.ans

# source:https://leetcode.cn/submissions/detail/585379179/
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        row, col = len(board), len(board[0])
        def find(x, y):
            ans = 0
            way = [[1,0],[0,-1],[-1,0],[0,1]]
            for i, j in way:
                new_x = x + i
                new_y = y + j
                while 0 <= new_x < row and 0 <= new_y < col:
                    if board[new_x][new_y] == 'B':
                        break
                    elif board[new_x][new_y] == 'p':
                        ans += 1
                        break
                    new_x += i
                    new_y += j
            return ans
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'R':
                    return find(i, j)