# source:https://leetcode.cn/problems/battleships-in-a-board/  dfs
from typing import List


class Solution:
    def dfs(self ,i ,j ,board ,sign):
        ans = False
        if board[i][j] == "X" and sign[i][j] == 0:
            sign[i][j] = 1
            ans = True
            for l, r in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ii = i + l
                jj = j + r
                if ii >= 0 and ii < len(board) and jj >= 0 and jj < len(board[0]) and board[ii][jj] == "X" and sign[ii][jj] == 0:
                    ans = ans and self.dfs(ii, jj, board, sign)
        return ans

    def countBattleships(self, board: List[List[str]]) -> int:
        row = len(board)
        column = len(board[0])
        if row == 1 and column == 1:
            if board[0][0] == "X":
                return 1
            else:
                return 0

        sign = [[0, ] * len(board[0]) for _ in range(len(board))]
        mx = 0
        for i in range(row):
            for j in range(column):
                if self.dfs(i, j, board, sign):
                    mx += 1
        return mx

