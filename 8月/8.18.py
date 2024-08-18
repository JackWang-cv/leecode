# source: https://leetcode.cn/problems/permutation-in-string/description/ 滑窗
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def judge(value):
            if new_d[value] == d[value] and not require.get(value,0):
                require[value] = require.get(value, 0) + 1
            elif new_d[value] != d[value] and require.get(value,0):
                del require[value]
            
        total_s = len(s1)
        d = Counter(s1)
        total_cato = len(d)
        i = 0
        new_d = {}
        require = {}
        for j, v in enumerate(s2):
            if v in d.keys():
                new_d[v] = new_d.get(v, 0) + 1
                judge(v)
            if j-i+1 > total_s:
                if new_d.get(s2[i],0):
                    new_d[s2[i]] -= 1
                    judge(s2[i])
                    if not new_d[s2[i]]:
                        del new_d[s2[i]]
                i += 1
            if j-i+1 == total_s and len(require) == total_cato:
                return True
        return False
        