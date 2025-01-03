# source:https://leetcode.cn/problems/accounts-merge/submissions/585985896/ 并查集
class union:
    def __init__(self, n):
        self.f = list(range(n))
    def find(self, x):
        if x == self.f[x]:
            return x
        else:
            self.f[x] = self.find(self.f[x])
            return self.f[x]
    def union(self, x, y):
        ori1 = self.find(x)
        ori2 = self.find(y)
        self.f[ori1] = ori2

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToIndex = dict()
        emailToName = dict()

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in emailToIndex:
                    emailToIndex[email] = len(emailToIndex)
                    emailToName[email] = name
        
        uf = union(len(emailToIndex))
        for account in accounts:
            first = emailToIndex[account[1]]
            for email in account[2:]:
                uf.union(first, emailToIndex[email])
        
        indextoEmails = defaultdict(list)
        for email, index in emailToIndex.items():
            index = uf.find(index)
            indextoEmails[index].append(email)
        
        ans = []
        for emails in indextoEmails.values():
            ans.append([emailToName[emails[0]]] + sorted(emails))
        
        return ans

# source:https://leetcode.cn/submissions/detail/585992858/ 模拟
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = version1.split('.')
        l2 = version2.split('.')
        def find(s):
            j = 0
            while j < len(s) and s[j] == '0':
                j += 1
            if j == len(s):
                res = '0'
            else:
                res = s[j:]
            return int(res)

        if len(l1) < len(l2):
            l1 += ['0' for _ in range(len(l2)-len(l1))]
        elif len(l1) > len(l2):
            l2 += ['0' for _ in range(len(l1)-len(l2))]

        for i in range(len(l1)):
            t1 = find(l1[i])
            t2 = find(l2[i])
            if t1 < t2:
                return -1
            elif t1 > t2:
                return 1
        return 0
                