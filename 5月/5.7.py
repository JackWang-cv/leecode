# source: https://leetcode.cn/problems/longest-palindromic-substring/
class Solution:
    def judge(self, s, l, r, string):
        if l < 0 or r == len(s):
            return string
        if s[l] == s[r]:
            if l + 1 == r:
                string = string + s[r]
            else:
                string = s[l] + string + s[r]
            string = self.judge(s, l - 1, r + 1, string)
        return string

    def longestPalindrome(self, s: str) -> str:
        s = list(s)
        mx = ''
        for i in range(len(s)):
            res = self.judge(s, i - 1, i + 1, s[i])
            if len(mx) < len(res):
                mx = res
            res = self.judge(s, i, i + 1, s[i])
            if len(mx) < len(res):
                mx = res
        return mx
