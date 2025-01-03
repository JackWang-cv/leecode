# source:https://leetcode.cn/problems/check-if-move-is-legal/description/ 枚举
from typing import List


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        ori = [[1, 0], [0, -1], [-1, 0], [0, 1], [1, 1], [1, -1], [-1, -1], [-1, 1]]
        d = {"W": "B", "B": "W"}
        for x, y in ori:
            new_x = rMove + x
            new_y = cMove + y
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
                if board[new_x][new_y] == d[color]:
                    while 1:
                        new_x += x
                        new_y += y
                        if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
                            if board[new_x][new_y] == color:
                                return True
                            elif board[new_x][new_y] == d[color]:
                                continue
                        break
        return False

# source:https://leetcode.cn/problems/h-index-ii/description/ 二分


class Solution1:
    def hIndex(self, citations: List[int]) -> int:

        # for i in range(len(citations)):
        #     t = len(citations)-i
        #     if t <= citations[i]:
        #         return min(t, citations[i])
        # return 0

        i = 0
        j = len(citations) - 1
        ans = 0
        while i <= j:
            mid = (i + j) // 2
            t = len(citations) - mid
            if t <= citations[mid]:
                ans = max(ans, min(t, citations[mid]))
                j = mid - 1
            else:
                i = mid + 1
        return ans

