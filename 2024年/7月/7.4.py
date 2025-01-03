# source:https://leetcode.cn/problems/minimum-size-subarray-sum/description/
from math import inf
from typing import List, Optional


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = count = j = i = 0
        mn = inf
        for i in range(len(nums)):
            s += nums[i]
            count += 1
            if s>=target:
                while s>=target:
                    mn = min(mn, count)
                    s -= nums[j]
                    j += 1
                    count -= 1

        return mn if mn!=inf else 0


# source:https://leetcode.cn/problems/count-complete-tree-nodes/description/
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:  # 法一 前序
    def find(self, p):
        if p == None:
            return 0
        return self.find(p.left)+self.find(p.right)+1

    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.find(root)


class Solution2:  # 二分+递归
    # 求二叉树的深度
    def height(self, root: TreeNode):
        height = 0
        while root:
            root = root.left
            height += 1

        return height

    def countNodes(self, root: TreeNode) -> int:
        # 空树，节点数为 0
        if root == None:
            return 0
        # 求左子树和右子树的深度
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        # 如果左子树的深度 = 右子树的深度，左子树为满二叉树
        # 节点数 = 左子树的深度 + 右子树的深度 + 根节点
        if leftHeight == rightHeight:
            return (2 ** leftHeight - 1) + self.countNodes(root.right) + 1
        # 如果左子树的深度 ＞ 右子树的深度，右子树为满二叉树
        # 节点数 = 左子树的深度 + 右子树的深度 + 根节点
        else:
            return (2 ** rightHeight - 1) + self.countNodes(root.left) + 1


