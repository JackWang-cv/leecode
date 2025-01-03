# source:https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d = Counter(p)
        new_d = {}
        require = {}
        res = []
        i = 0
        for j, v in enumerate(s):
            if v in d.keys():
                new_d[v] = new_d.get(v, 0) + 1
                if new_d[v] == d[v] and not require.get(v, 0):
                    require[v] = 1
                elif new_d[v] != d[v] and require.get(v, 0):
                    del require[v]
            if j - i + 1 > len(p):
                if new_d.get(s[i],0):
                    new_d[s[i]] -= 1
                    if new_d[s[i]] == d[s[i]] and not require.get(s[i], 0):
                        require[s[i]] = 1
                    elif new_d[s[i]] != d[s[i]] and require.get(s[i], 0):
                        del require[s[i]]
                    if not new_d[s[i]]:
                        del new_d[s[i]]
                i += 1
            if j - i + 1 == len(p) and len(require) == len(d):
                res.append(i)
        return res