# source:https://leetcode.cn/submissions/detail/576974671/ 前缀和+dfs
# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        ans = 0
        d = defaultdict(int)
        def find(p, record):
            nonlocal ans
            for i in range(len(record)-1):
                if record[i] == record[-1] - targetSum:
                    # print(d, record[i])
                    ans += d[record[i]] if targetSum != 0 else d[record[i]]-1
                    break
            if p.left:
                d[record[-1]+p.left.val] += 1
                find(p.left, record + [record[-1]+p.left.val])
                d[record[-1]+p.left.val] -= 1
            if p.right:
                d[record[-1]+p.right.val] += 1
                find(p.right, record + [record[-1]+p.right.val])
                d[record[-1]+p.right.val] -= 1
        d[0] += 1
        d[root.val] += 1
        find(root, [0, root.val])
        return ans