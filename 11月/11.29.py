# source:https://leetcode.cn/submissions/detail/583867043/ 01背包
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        temp = sum(nums)
        if temp & 1:
            return False
        target = temp//2
        f = [[False]*(target+1) for _ in range(n+1)]
        f[0][0] = True
        for i, x in enumerate(nums):
            for c in range(target+1):
                if x > c:
                    f[i+1][c] = f[i][c]
                else:
                    f[i+1][c] = f[i][c-x] | f[i][c]
        # print(f)
        return f[-1][-1]
    

# source:https://leetcode.cn/submissions/detail/583869658/
# 法一: LCS 
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        f = [[0]*(n2+1) for _ in range(n1+1)]
        for i, x in enumerate(word1):
            for j, c in enumerate(word2):
                if x != c:
                    f[i+1][j+1] = max(f[i][j+1], f[i+1][j])
                else:
                    f[i+1][j+1] = f[i][j] + 1
        return n1 + n2 - 2*f[-1][-1]
# 法二：参考编辑距离
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        f = [[0]*(n2+1) for _ in range(n1+1)]
        f[0] = range(n2+1)
        for i, x in enumerate(word1):
            f[i+1][0] = i+1
            for j, c in enumerate(word2):
                if x == c:
                    f[i+1][j+1] = f[i][j]
                else:
                    f[i+1][j+1] = min(f[i][j+1], f[i+1][j])+1
        return f[-1][-1]

# source:https://leetcode.cn/submissions/detail/583882034/ 贪心
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = ''
        while a > 0 and b > 0:
            if a > b:
                ans += 'aab'
                a-=2
                b-=1
            elif a < b:
                ans += 'bba'
                b-=2
                a-=1
            else:
                ans += 'ab'*a
                a-=a
                b-=b
        if a > 0:
            ans += 'a'*a
        elif b > 0:
            ans += 'b'*b
        return ans
