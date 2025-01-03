# source: https://leetcode.cn/problems/sum-root-to-leaf-numbers/ dfs
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def find(p, s):
            nonlocal res
            if not p.left and not p.right:
                res += int(s)
                return
            if p.left:
                find(p.left, s + str(p.left.val))
            if p.right:
                find(p.right, s + str(p.right.val))
        find(root, str(root.val))
        return res

# source:https://leetcode.cn/problems/sum-of-square-numbers/description/ 双指针
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(pow(c, 0.5))
        while i <= j:
            total = i**2 + j**2
            if total == c:
                return True
            elif total < c:
                i += 1
            else:
                j -= 1
        return False