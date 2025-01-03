# source:https://leetcode.cn/problems/zigzag-conversion/  字符串
from cmath import inf


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for _ in range(numRows)]
        index, direction = 0, 0
        for value in s:
            if index < 0:
                index = 0
            if index >= numRows:
                index = numRows-1
            
            if index == 0:
                direction = 1
            elif index == numRows-1:
                direction = -1
            res[index].append(value)
            index += direction
        # print(res)
        ans = ''
        for row in res:
            ans += ''.join(row)
        return ans

# source:https://leetcode.cn/problems/length-of-the-longest-subsequence-that-sums-to-target/ 01背包
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        f = [[-inf for _ in range(target+1)] for _ in range(len(nums)+1)]
        f[0][0] = 0
        for i, x in enumerate(nums):
            for j in range(target+1):
                if j < x:
                    f[i+1][j] = f[i][j]
                else:
                    
                    f[i+1][j] = max(f[i][j], f[i][j-x]+1)
        return f[-1][-1] if f[-1][-1]!=-inf else -1

# source:https://leetcode.cn/problems/ones-and-zeroes/submissions/584094846/ 01背包三维
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        f = [[[0]*(n+1) for _ in range(m+1)] for _ in range(len(strs)+1)]
        for i in range(len(strs)):
            zeros = strs[i].count('0')
            ones = strs[i].count('1')
            for j in range(m+1):
                for k in range(n+1):
                    if j >= zeros and k >= ones:
                        f[i+1][j][k] = max(f[i][j][k], f[i][j-zeros][k-ones]+1)
                    else:
                        f[i+1][j][k] = f[i][j][k]
        
        return f[-1][-1][-1]
