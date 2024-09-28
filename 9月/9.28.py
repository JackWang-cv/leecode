# source:https://leetcode.cn/problems/restore-ip-addresses/description/
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def dfs(index, t):
            if len(t) == 4 and index == len(s):
                ans.append('.'.join(t))
            if index == len(s):
                return 
            if s[index] == '0':
                dfs(index+1, t + ['0'])
            else:
                for i in range(index, len(s), 1):
                    if 0 <= int(s[index:i+1]) <= 255:
                        dfs(i+1, t + [s[index:i+1]])
        dfs(0, [])
        return ans