# 手写矩阵连乘最小次数的 dp
from math import inf
from typing import List


def matrix_chain_order(p):
    """
    :param p: List[int]，表示矩阵链的维度，比如 p = [10, 20, 30] 表示两个矩阵
              A1: 10x20, A2: 20x30。
    :return: 最少的标量乘法次数。
    """
    n = len(p) - 1  # 矩阵数量
    # 初始化 DP 表
    f = [[0] * n for _ in range(n)]

    # 按照区间长度递推
    for length in range(2, n + 1):  # 区间长度从 2 到 n
        for i in range(n - length + 1):  # 左端点
            j = i + length - 1  # 右端点
            f[i][j] = float('inf')  # 初始化为无穷大
            for k in range(i, j):  # 枚举分割点
                cost = f[i][k] + f[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                print(f'{cost=}')
                f[i][j] = min(f[i][j], cost)
        print(f)
    return f[0][n - 1]  # 返回从 A1 到 An 的最优解

result = matrix_chain_order([10, 20, 30, 40, 30])
print(result)  # 输出: 30000

# source:https://leetcode.cn/problems/coin-change/ 类似完全背包 dp
# 完全背包dp递推：
# f[i+1][c] = max(f[i][c], f[i+1][c - w[i]]+v[i])
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [[inf for _ in range(amount+1)] for _ in range(len(coins)+1)]
        coins.sort()
        f[0][0] = 0
        for i, x in enumerate(coins):
            for c in range(amount+1):
                if c < x:
                    f[i+1][c] = f[i][c]
                else:
                    if f[i][c] == 0:
                        f[i+1][c] = f[i+1][c - x]+1
                    else:
                        f[i+1][c] = min(f[i][c], f[i+1][c - x]+1)
        # print(f)
        ans = f[i+1][amount]
        return ans if ans < inf else -1
# source:https://leetcode.cn/problems/coin-change-ii/ 和上题一样 换了种问法
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        f = [[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]
        f[0][0] = 1
        for i, x in enumerate(coins):
            for c in range(amount+1):
                if c < x:
                    f[i+1][c] = f[i][c]
                else:
                    f[i+1][c] = f[i][c] + f[i+1][c-x]
        # print(f)
        return f[i+1][-1]