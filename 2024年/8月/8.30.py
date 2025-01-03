# source:https://leetcode.cn/problems/shortest-and-lexicographically-smallest-beautiful-string/description/
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        i = 0
        count = 0
        res = len(s)+1
        new_s = ''
        for j, v in enumerate(s):
            if v == '1':
                count += 1
            while count == k and i <= j:
                if res > j-i+1:
                    res = j-i+1 
                    new_s = s[i:j+1]
                elif res == j-i+1:
                    new_s = min(new_s, s[i:j+1])
                if s[i] == '1':
                    count -= 1
                i += 1
        return new_s
X = Solution()
X.shortestBeautifulSubstring('100011001', 3)