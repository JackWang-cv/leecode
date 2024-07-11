# source:https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-i/description/ 双指针
from typing import List, Optional


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        l = 1
        while l < n and nums[l - 1] < nums[l]:
            l += 1
        res += l + (l < n)
        for r in range(n - 2, -1, -1):
            while l > 0 and nums[l - 1] >= nums[r + 1]:
                l -= 1
            res += l + (l <= r)
            if nums[r] >= nums[r + 1]:
                break
        return res

# source: https://leetcode.cn/problems/nth-digit/description/ logit


class Solution1:
    def findNthDigit(self, n: int) -> int:
        i = 0
        ini = 1
        while n > 0:
            n -= 9 * pow(10, i) * (i + 1)
            ini *= 10
            i += 1
        else:
            n += 9 * pow(10, i - 1) * (i)
            ini /= 10

        first = (n - 1) // i
        second = (n - 1) % i

        return int(str(first + ini)[second])

# source:https://leetcode.cn/problems/recover-binary-search-tree/description/ dfs


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution2:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        k = 0
        res = []

        def find(p, i):
            if p == None:
                return
            find(p.left, i)
            nonlocal k
            if i:
                res.append(p.val)
            else:
                p.val = res[k]
                k += 1
            find(p.right, i)

        find(root, 1)
        res.sort()
        find(root, 0)


