# source:https://leetcode.cn/problems/find-the-winning-player-in-coin-game/
class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        d = {0:'Alice', 1:'Bob'}
        key = 1
        while x >= 1 and y >= 4:
            x -= 1
            y -= 4
            key ^= 1
        return d[key]

# source:https://leetcode.cn/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/ 二维前缀和+二分
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        d = [[0 for _ in range(len(grid)+1)] for _ in range(len(grid[0]))]
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                d[j][i+1] = d[j][i] + grid[i][j]
        # print(d)
        ans = 0
        total = [[0 for _ in range(len(grid[0])+1)] for _ in range(len(grid))]
        for i in range(len(total)):
            for j in range(1, len(total[0])):
                total[i][j] = total[i][j-1] + d[j-1][i+1]
        # print(total)

        for i in range(len(total)):
            left = 1
            right = len(total[i])
            while left < right:
                mid = (left+right)//2
                if total[i][mid] <= k:
                    left = mid+1
                else:
                    right = mid
            ans += left-1
        return ans

# new way:模板 Link : https://leetcode.cn/problems/range-sum-query-2d-immutable/solutions/2667331/tu-jie-yi-zhang-tu-miao-dong-er-wei-qian-84qp/
# s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + x 
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + x
                if s[i + 1][j + 1] <= k:
                    ans += 1
        return ans
