# source:https://leetcode.cn/problems/maximum-average-subarray-i/description/ 定长窗口
from cmath import inf
from collections import Counter
from typing import List, Optional


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp = sum(nums[:k])
        mx = temp/k
        j = 0
        for i in range(k, len(nums)):
            temp += nums[i] - nums[j]
            mx = max(temp/k, mx)
            j += 1
        return mx

# source: https://leetcode.cn/problems/subtree-of-another-tree/ dfs
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def comp(p, sub):
            if not p and not sub:
                return True
            elif not p and sub:
                return False
            elif p and not sub:
                return False
            elif p.val != sub.val:
                return False
            else:
                return comp(p.left, sub.left) and comp(p.right, sub.right)

        def fun(p):
            if not p:
                return False
            flag = False
            if p.val == subRoot.val:
                flag = comp(p, subRoot)
                
            flag = flag or fun(p.left)
            flag = flag or fun(p.right)
            return flag
        return fun(root)

# source:https://leetcode.cn/problems/replace-the-substring-for-balanced-string/description/ 滑动窗口求最小长度
# 根据题意，如果在待替换子串之外的任意字符的出现次数超过 m= n/4.​
# 那么无论怎么替换，都无法使这个字符在整个字符串中的出现次数为 m。
# 反过来说，如果在待替换子串之外的任意字符的出现次数都不超过 m，那么可以通过替换，使 s 为平衡字符串，即每个字符的出现次数均为 m。


class Solution:
    def balancedString(self, s: str) -> int:
        m = len(s) // 4
        cnt = Counter(s)
        if len(cnt) == 4 and min(cnt.values()) == m:  # 已经符合要求啦
            return 0
        ans, left = inf, 0
        for right, c in enumerate(s):  # 枚举子串右端点
            cnt[c] -= 1
            while max(cnt.values()) <= m:
                ans = min(ans, right - left + 1)
                cnt[s[left]] += 1
                left += 1  # 缩小子串
        return ans

# source:https://leetcode.cn/problems/count-complete-subarrays-in-an-array/description/ 变成长滑动窗口
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        res = 0
        d = Counter(nums)
        length = len(d)
        i = j = 0
        temp = {}
        for j in range(len(nums)):
            temp[nums[j]] = temp.get(nums[j], 0) + 1
            while len(temp) == length:
                res += len(nums) - j
                temp[nums[i]] -= 1
                if temp[nums[i]] == 0:
                    del temp[nums[i]]
                i += 1
        return res

# source:https://leetcode.cn/problems/fruit-into-baskets/description/
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i = j = res = 0
        full = {}
        while j < len(fruits):
            full[fruits[j]] = full.get(fruits[j], 0) + 1
            while len(full) > 2:
                full[fruits[i]] -= 1
                if not full[fruits[i]]:
                    del full[fruits[i]]
                i += 1
            res = max(res, j-i+1)
            j += 1
        return res