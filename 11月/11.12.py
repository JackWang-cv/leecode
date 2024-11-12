# source:https://leetcode.cn/submissions/detail/579969711/ 栈 哈希表
class Solution:
    def clearStars(self, s: str) -> str:
        d = defaultdict(list)
        delete = [1 for _ in range(len(s))]
        for i, v in enumerate(s):
            if v == '*':
                res = sorted(d.keys())[0]
                # print(d, res)
                x = d[res].pop()
                if d[res] == []:
                    del d[res]
                delete[x] = 0
            else:
                d[v].append(i)
        ans = ''
        for i,v in enumerate(s):
            if delete[i] and v != '*':
                ans += v
        return ans

# source:https://leetcode.cn/submissions/detail/579916632/ 滑窗 前缀和
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        judge = [False for _ in range(len(s)+1)]
        total_0 = [0 for _ in range(len(s)+1)]
        total_1 = [0 for _ in range(len(s)+1)]
        for i, v in enumerate(s):
            if v == '1':
                total_1[i+1] = total_1[i] + 1
                total_0[i+1] = total_0[i]
            else:
                total_0[i+1] = total_0[i] + 1
                total_1[i+1] = total_1[i]
        # print(total_0, total_1)
        ans = 0
        i = 0
        for j in range(1, len(total_0)):
            while total_0[j] - total_0[i] > k and total_1[j] - total_1[i] > k:
                i += 1
            # print(i, j)
            ans += j-i
        return ans