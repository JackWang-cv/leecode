# source:https://leetcode.cn/problems/find-longest-special-substring-that-occurs-thrice-i/ hashdict,双指针

class Solution:
    def maximumLength(self, s: str) -> int:
        hashDict = {}
        res = -1
        i = 0
        while i < len(s):
            j = i
            while j < len(s):
                if s[j] == s[i]:
                    hashDict[s[i:j + 1]] = hashDict.get(s[i:j + 1], 0) + 1  # 0是没有这个键就默认值0
                    if hashDict.get(s[i:j + 1], 0) >= 3:
                        res = max(res, j + 1 - i)
                    j += 1
                else:
                    break
            i += 1

        return res