# source:https://leetcode.cn/problems/merge-nodes-in-between-zeros/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        t = head
        while p:
            if p.val == 0:
                t.next = p.next
                t = p.next
                if t:
                    p = t.next
                else:
                    break
            else:
                t.val += p.val
                p = p.next
        return head.next

from sortedcontainers import SortedList
from collections import deque
from typing import List
class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        def bfs(i, j, count):
            q = deque()
            q.append([i, j])
            visit[i][j] = 1
            while q:
                x, y = q.popleft()
                count += 1
                for m, n in [[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1]]:
                    new_x = x + m
                    new_y = y + n
                    if 0 <= new_x < len(land) and 0 <= new_y < len(land[0]):
                        if land[new_x][new_y] == 0 and not visit[new_x][new_y]:
                            visit[new_x][new_y] = 1
                            q.append([new_x, new_y])
            return count
        visit = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
        ans = SortedList()
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 0 and not visit[i][j]:
                    ans.add(bfs(i, j, 0))
        return list(ans)