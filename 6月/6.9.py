# source:https://leetcode.cn/problems/path-sum/  递归

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find(self, r, t, s):
        if r.left==None and r.right==None:
            if s+r.val==t:
                return True
            else:
                return False
        flag = False
        if r.left!=None:
            flag = flag or self.find(r.left, t, s+r.val)
        if r.right!=None:
            flag = flag or self.find(r.right, t, s+r.val)
        return flag

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root==None:
            return False
        return self.find(root, targetSum, 0)
