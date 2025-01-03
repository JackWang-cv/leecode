# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 辅助函数，递归反转链表
        def exchange(node, count):
            nonlocal start, left_node, e_node, right_node
            if count == left - 1:  # 找到 left 前一个节点
                start = node
                left_node = node.next
            elif count == right:  # 找到 right 节点
                e_node = node
                right_node = node.next
                return
            exchange(node.next, count + 1)
            if count >= left and count < right:  # 反转 left 到 right 之间的节点
                node.next.next = node

        if left == right:
            return head  # 如果 left == right，直接返回原链表

        dummy = ListNode(0)  # 虚拟头节点
        dummy.next = head
        start, left_node, e_node, right_node = None, None, None, None

        exchange(dummy, 0)  # 从虚拟头节点开始递归
        
        # 修复链表的连接
        start.next = e_node  # 将 left 之前的节点连接到反转后的子链表
        left_node.next = right_node  # 将反转后的子链表连接到 right 后面的部分

        return dummy.next


# 创建链表 [1,2,3,4,5]
node5 = ListNode(5)
# node4 = ListNode(4, node5)
# node3 = ListNode(3, node4)
# node2 = ListNode(2, node3)
# node1 = ListNode(1, node2)

solution = Solution()
new_head = solution.reverseBetween(node5, 1, 1)

