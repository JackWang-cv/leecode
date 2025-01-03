# source:https://leetcode.cn/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        k = 1
        s1 = s2 = 0
        while l1 != None:
            s1 += l1.val * k
            l1 = l1.next
            k *= 10
        k = 1
        while l2 != None:
            s2 += l2.val * k
            l2 = l2.next
            k *= 10
        res = s1 + s2
        L = list(str(res))
        l3 = ListNode(int(L[-1]))
        p = l3
        c = len(L) - 2
        while c >= 0:
            t = ListNode(int(L[c]))
            p.next = t
            p = p.next
            c -= 1
        return l3
