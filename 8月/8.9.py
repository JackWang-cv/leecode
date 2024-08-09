# source:https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/ 滑窗+平衡树
from typing import List
from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        s = SortedList()
        n = len(nums)
        left = right = ret = 0

        while right < n:
            s.add(nums[right])
            while s[-1] - s[0] > limit:
                s.remove(nums[left])
                left += 1
            ret = max(ret, right - left + 1)
            right += 1
        
        return ret

# source:https://leetcode.cn/problems/minimum-window-substring/description/ 滑动窗口
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        d = Counter(t)  # 统计 t 中每个字符的频率
        required = len(d)  # 需要匹配的字符种类数量
        check = {}
        l, r = 0, 0
        formed = 0  # 当前已经满足的字符种类数
        res = (float("inf"), None, None)  # (窗口长度, 左指针, 右指针)
        
        while r < len(s):
            char = s[r]
            check[char] = check.get(char, 0) + 1
            
            if char in d and check[char] == d[char]:
                formed += 1
            
            # 尝试收缩窗口
            while l <= r and formed == required:
                char = s[l]
                
                # 更新最小窗口
                if r - l + 1 < res[0]:
                    res = (r - l + 1, l, r)
                
                check[char] -= 1
                if char in d and check[char] < d[char]:
                    formed -= 1
                
                l += 1
            
            r += 1
        
        return "" if res[0] == float("inf") else s[res[1]:res[2] + 1]

