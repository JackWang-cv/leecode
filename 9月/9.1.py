# source:https://leetcode.cn/problems/swap-nodes-in-pairs/description/
# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def exchange(node):
            if node == None:
                return None
            elif node.next == None:
                return node
            v = exchange(node.next.next)
            q = node.next
            q.next = node
            node.next = v 
            return q

        if head == None or head.next == None:
            return head
        return exchange(head)

# source:https://leetcode.cn/problems/daily-temperatures/description/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = []
        for i, v in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < v:
                t = stack.pop()
                count = i - t
                res[t] = count
            stack.append(i)
        return res