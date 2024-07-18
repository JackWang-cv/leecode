# source: https://leetcode.cn/problems/arranging-coins/description/ 二分
from typing import List


class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        j = n
        while i <= j:

            mid = (i + j) // 2
            t = (1 + mid) * mid // 2
            if 0 <= n - t < mid + 1:
                return mid
            elif n - t >= mid + 1:
                i = mid + 1
            else:
                j = mid - 1

# source: https://leetcode.cn/problems/max-increase-to-keep-city-skyline/description/ 贪心

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        def search(first, second, K):
            for i in range(first):
                t_m = -1
                for j in range(second):
                    if K:
                        t_m = max(t_m, grid[j][i])
                    else:
                        t_m = max(t_m, grid[i][j])
                ori[K].append(t_m)

        ori = [[] for _ in range(2)]
        L1 = len(grid)
        L2 = len(grid[0])
        d = [[L1, L2], [L2, L1]]
        res = 0
        for i in range(2):
            search(d[i][0], d[i][1], i)

        for i in range(L1):
            for j in range(L2):
                temp = min(ori[0][i], ori[1][j]) - grid[i][j]
                if temp > 0:
                    res += temp
        return res


