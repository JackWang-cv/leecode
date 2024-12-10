# source:https://leetcode.cn/problems/knight-dialer/ 记忆化搜索
MOD = 1_000_000_007
NEXT = (4, 6), (6, 8), (7, 9), (4, 8), (0, 3, 9), (), (0, 1, 7), (2, 6), (1, 3), (2, 4)

@cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
def dfs(i: int, j: int) -> int:
    if i == 0:
        return 1
    return sum(dfs(i - 1, k) for k in NEXT[j]) % MOD

class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        return (sum(dfs(n - 1, j) for j in range(10))) % MOD

