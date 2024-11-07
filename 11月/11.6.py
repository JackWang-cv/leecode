# source:https://leetcode.cn/submissions/detail/578498236/ 滑窗
from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        store = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                store.append(1)
            else:
                store.append(0)
        i = cnt = 0
        ans = []
        for j , v in enumerate(store):
            cnt += v
            if j-i+2 > k:
                cnt -= store[i]
                i += 1
            if j-i+2 == k:
                if cnt == k-1:
                    ans.append(nums[j+1])
                else:
                    ans.append(-1)
        return ans

# source:https://leetcode.cn/submissions/detail/578385112/
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        ans = 0
        res = [[[0, 0] for _ in range(len(grid[0])+1)] for _ in range(len(grid)+1)]
        for i in range(1, len(res)):
            for j in range(1, len(res[0])):
                res[i][j][0] = res[i-1][j][0]+res[i][j-1][0]-res[i-1][j-1][0]
                res[i][j][1] = res[i-1][j][1]+res[i][j-1][1]-res[i-1][j-1][1]
                if grid[i-1][j-1] == 'X':
                    res[i][j][0] += 1
                elif grid[i-1][j-1] == 'Y':
                    res[i][j][1] += 1
                        
                if res[i][j][0]>0 and res[i][j][0] == res[i][j][1]:
                    ans += 1
        # print(res)
        return ans

# source:https://leetcode.cn/submissions/detail/578379094/
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and j == 0:
                    matrix[i][j] = matrix[i][j]
                elif i == 0 :
                    matrix[i][j] = matrix[i][j-1]^matrix[i][j]
                elif j == 0:
                    matrix[i][j] = matrix[i-1][j]^matrix[i][j]
                else:
                    matrix[i][j] = matrix[i-1][j]^matrix[i][j-1]^matrix[i-1][j-1]^matrix[i][j]
                res.append(matrix[i][j])
        res.sort()
        return res[-1*k]

# source:https://leetcode.cn/submissions/detail/578321205/
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
