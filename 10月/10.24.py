# source:https://leetcode.cn/submissions/detail/575303332/ 贪心
from collections import defaultdict
from typing import List


class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        i = 0
        count = 0
        for j, v in enumerate(skills):
            if skills[i] < v:
                i = j
                count = 1  
            elif j > i:
                count += 1
            if count >= k:
                return i
        return i

# source:https://leetcode.cn/submissions/detail/575314034/ 前缀， 后缀
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = defaultdict(int)
        pre = [set() for _ in range(len(s)+1)]
        suf = [set() for _ in range(len(s)+1)]
        i = 0
        j = len(s)-1
        pre_set = set()
        suf_set = set()
        while i < len(s):
            pre_set.add(s[i])
            suf_set.add(s[j])
            pre[i+1] = pre_set.copy()
            suf[j] = suf_set.copy()
            i += 1 
            j -= 1
        for i, v in enumerate(s):
            t = pre[i].intersection(suf[i+1])
            if not t:
                continue
            for value in t:
                ans[value+v+value] += 1
        print(ans)
        return len(ans.keys())
