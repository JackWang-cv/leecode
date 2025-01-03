# source：https://leetcode.cn/problems/split-array-largest-sum/description/ 贪心+二分
# 「使……最大值尽可能小」是二分搜索题目常见的问法。
from typing import List, Optional


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(x) -> bool:
            total, cnt = 0, 1
            # 统计符合区间的个数
            for n in nums:
                if total + n > x:
                    cnt += 1
                    total = n
                else:
                    total += n
            return cnt <= k
        # 利用最大值和总和进行二分找最大值尽可能小
        i = max(nums)
        j = sum(nums)
        while i < j:
            mid = (i + j) // 2
            if check(mid):
                j = mid
            else:
                i = mid + 1
        return i

# source:https://leetcode.cn/problems/minimum-depth-of-binary-tree/description/ dfs


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def find(p) -> int:
            if p == None:
                return 0
            elif p.left==None and p.right!=None:
                return find(p.right)+1
            elif p.left!=None and p.right==None:
                return find(p.left)+1
            else:
                return min(find(p.left)+1,find(p.right)+1)
        return find(root)

# source:https://leetcode.cn/problems/path-sum-ii/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
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