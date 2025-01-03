# source: https://leetcode.cn/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        t = list()
        mx = 0
        total = 0
        for i in s:
            if i not in t:
                t.append(i)
                total+=1
            else:
                for j in range(len(t)):
                    if t[j] == i:
                        break
                t = t[j+1:]
                t.append(i)
                total = len(t)
            if total > mx:
                mx = total
        return mx
