# source:https://leetcode.cn/problems/length-of-the-longest-alphabetical-continuous-substring/description/
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        i = 0
        j = 1
        ans = 1
        while j < len(s):
            if ord(s[j])-ord(s[j-1]) != 1:
                i = j
            ans = max(ans, j-i+1)
            j += 1
            
        return ans