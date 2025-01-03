# source:https://leetcode.cn/problems/find-the-count-of-numbers-which-are-not-special/  折半 o(nlogn)
from collections import defaultdict


class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        # 统计是特殊数字的
        ans = 0
        left= int(pow(l, 0.5))
        right = int(pow(r, 0.5))
        if int(pow(l, 0.5)) != pow(l, 0.5):
            left += 1
        res = 0
        def judge(v):
            if v == 1:
                return 0
            elif v < 3:
                return 1
            for i in range(2, int(pow(v, 0.5))+1):
                if v % i == 0:
                    return 0
            return 1
            
        for i in range(left, right+1):
            if judge(i):
                res += 1
        return r - l + 1 - res

# source:https://leetcode.cn/problems/count-number-of-ways-to-place-houses/ dp
class Solution:
    def countHousePlacements(self, n: int) -> int:
        if n == 1:
            return 2*2
        f0, f1 = 1, 2
        MOD = pow(10, 9)+7
        for i in range(2, n+1):
            f0, f1 = f1, (f0+f1)%MOD
        return (f1**2) % MOD

# source:https://leetcode.cn/problems/n-queens/submissions/582389733/ N皇后 回溯(全排列plus)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        col = [0 for _ in range(n)]
        def valid(v, cnt):
            for i in range(cnt):
                if (i + col[i] == v + cnt) or (i - col[i] == cnt - v):
                    return 0
            return 1
        def dfs(s, cnt):
            if cnt == n:
                res = ['.'*c + 'Q' + '.'*(n-c-1) for c in col]
                ans.append(res)
                return 
            for v in s:
                if valid(v, cnt):
                    col[cnt] = v
                    dfs(s-{v}, cnt+1)
        dfs(set(range(n)), 0)
        return ans

# source:https://leetcode.cn/problems/n-queens-ii/ N皇后
class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        col = [0 for _ in range(n)]
        def dfs(s, cnt):
            nonlocal ans
            if cnt == n:
                ans += 1
                return 
            for v in s:
                if all([(i + col[i] != v + cnt) and (i - col[i] != cnt - v) for i in range(cnt)]):
                    col[cnt] = v
                    dfs(s-{v}, cnt+1)
        dfs(set(range(n)), 0)
        return ans
# 空间换时间优化
class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        col = [0 for _ in range(n)]
        d = defaultdict(int)
        d1 = defaultdict(int)
        def dfs(s, cnt):
            nonlocal ans
            if cnt == n:
                ans += 1
                return 
            for v in s:
                if d[v + cnt] == 0 and d1[cnt - v] == 0:
                    d[v + cnt]=1
                    d1[cnt - v]=1
                    col[cnt] = v
                    dfs(s-{v}, cnt+1)
                    d[v + cnt]=0
                    d1[cnt - v]=0
        dfs(set(range(n)), 0)
        return ans