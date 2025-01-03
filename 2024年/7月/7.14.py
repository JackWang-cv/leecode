# source:https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/description/ dfs
# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root
        d = deque()
        d.append(root)
        i = 1
        cnt = 0
        while len(d) > 0:
            t = d.popleft()
            cnt += 1
            if cnt == i:
                t.next = None
                i *= 2
                i += 1
            elif len(d) > 0:
                t.next = d[0]

            if t.left:
                d.append(t.left)
            if t.right:
                d.append(t.right)
        return root

# source:https://leetcode.cn/problems/find-if-array-can-be-sorted/description/
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        lastgroupmax = 0
        curgroupmax = 0
        cnt = 0
        for num in nums:
            if cnt == 0 :
                cnt = num.bit_count()
                curgroupmax  = num
            elif cnt == num.bit_count():
                curgroupmax = max(curgroupmax, num)
            else:
                lastgroupmax = curgroupmax
                curgroupmax = num
                cnt = num.bit_count()
            if num < lastgroupmax:
                return False
        return True


