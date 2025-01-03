# source:https://leetcode.cn/problems/lexicographically-smallest-string-after-substring-operation/description/

class Solution:
    def smallestString(self, s: str) -> str:
        if len(s) == 1:
            if s[0] == "a":
                return "z"
            return chr(ord(s[0]) - 1)

        if s[:-1] == "a" * (len(s) - 1):
            if s[-1] == "a":
                return s[:-1] + "z"
            return s[:-1] + chr(ord(s[-1]) - 1)

        flag = False
        new_s = ""

        for i in range(len(s)):
            if s[i] != "a":
                new_s += chr(ord(s[i]) - 1)
                flag = True
                continue

            if flag:
                new_s += s[i:]
                break
            new_s += s[i]
        return new_s