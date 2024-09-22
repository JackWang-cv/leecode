# source:https://leetcode.cn/problems/find-the-town-judge/description/
from collections import defaultdict, deque
from typing import List


class Solution1:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return 1 if n == 1 else -1
        d = defaultdict(list)
        count = defaultdict(int)
        for i, j in trust:
            count[j] += 1
            d[i].append(j)
        t = sorted(count.items(), key=lambda x:x[1])[-1]
        return t[0] if t[1] == n-1 and not d[t[0]] else -1

# source:https://leetcode.cn/problems/minesweeper/description/ bfs
from collections import deque
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # 如果点击的是地雷，游戏结束
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        visit = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        
        def bfs(i, j):
            q = deque([[i, j]])
            visit[i][j] = 1
            
            while q:
                x, y = q.popleft()
                count = 0
                # 统计相邻地雷数
                for m, n in [[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1]]:
                    new_x = x + m
                    new_y = y + n
                    if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
                        if board[new_x][new_y] == 'M':
                            count += 1
                
                if count > 0:
                    # 如果相邻有地雷，更新为地雷数量，不继续递归
                    board[x][y] = str(count)
                else:
                    # 没有地雷，更新为 'B' 并继续搜索相邻未挖的空方块
                    board[x][y] = 'B'
                    for m, n in [[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1]]:
                        new_x = x + m
                        new_y = y + n
                        if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and not visit[new_x][new_y] and board[new_x][new_y] == 'E':
                            q.append([new_x, new_y])
                            visit[new_x][new_y] = 1
        
        # 从点击点开始搜索
        bfs(click[0], click[1])
        return board
