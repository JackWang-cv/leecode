# source:https://leetcode.cn/problems/removing-stars-from-a-string/description/ 栈
from collections import deque
from typing import List, Optional


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for v in s:
            if not stack:
                stack.append(v)
                continue
            if v == '*':
                stack.pop()
            else:
                stack.append(v)
        return ''.join(stack)

# source:https://leetcode.cn/problems/spiral-matrix-ii/description/ 模拟
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        i = j = 0
        k = 0
        num = 1
        while num <= pow(n,2):
            res[i][j] = num
            if i == k and j < n - k - 1:
                j += 1
            elif i < n - k - 1 and j == n - k - 1:
                i += 1
            elif i == n - k - 1 and j > k:
                j -= 1
            elif i > k + 1 and j == k:
                i -= 1
            if i == k+1 and j == k:
                k += 1
            num += 1
            print(res)
        return res

# source：https://leetcode.cn/problems/coloring-a-border/description/ bfs
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        visit = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        judge = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def bfs(i, j):
            q = deque()
            q.append([i, j])
            visit[i][j] = 1
            while q:
                x, y = q.popleft()
                for m, n in [[1,0],[0,-1],[-1,0],[0,1]]:
                    new_x = x + m
                    new_y = y + n
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                        if grid[new_x][new_y] != grid[x][y]:
                            judge[x][y] = 1
                        elif grid[new_x][new_y] == grid[x][y] and (x == 0 or x == len(grid)-1 or y == 0 or y == len(grid[0])-1): 
                            judge[x][y] = 1
                        if not visit[new_x][new_y] and grid[new_x][new_y] == grid[x][y]:
                            visit[new_x][new_y] = 1
                            q.append([new_x, new_y])

        bfs(row, col)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if judge[i][j] == 1:
                    grid[i][j] = color
        return grid

# source:https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode(0, head)

        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next