# source: https://leetcode.cn/problems/split-array-largest-sum/ 二分
from typing import List, Optional


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(x) -> bool:
            total, cnt = 0, 1
            for n in nums:
                if total + n > x:
                    cnt += 1
                    total = n
                else:
                    total += n
            return cnt <= k

        i = max(nums)
        j = sum(nums)
        while i < j:
            mid = (i + j) // 2
            if check(mid):
                j = mid
            else:
                i = mid + 1
        return i

# source:https://leetcode.cn/problems/path-sum-ii/ 递归 dfs
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def find(x, L):
            if not x:
                return
            if not x.left and not x.right:
                if sum(L) + x.val == targetSum:
                    res.append(L + [x.val])
            find(x.left, L + [x.val])
            find(x.right, L + [x.val])

        find(root, [])
        return res