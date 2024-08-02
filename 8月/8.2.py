# source:https://leetcode.cn/problems/right-triangles/description/
from typing import List


class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        res = 0
        m1 = [[0 for _ in range(len(grid[0])+2)] for _ in range(len(grid)+2)]
        m2 = [[0 for _ in range(len(grid[0])+2)] for _ in range(len(grid)+2)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                m1[i+1][j+1] = m1[i+1][j] + grid[i][j]
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                m2[i+1][j+1] = m2[i][j+1] + grid[i][j]
        # print(m1,m2)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += (m1[i+1][-2]-1)*(-1 + m2[len(m2)-2][j+1])
        return res

# source:https://leetcode.cn/problems/find-the-k-beauty-of-a-number/description/
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        res = 0
        string = str(num)
        for i in range(len(string)-k+1):
            if string[i] == '0':
                ind = i
                while ind < i+k:
                    if string[ind] == '0':
                        ind += 1
                    else:
                        break
                else:
                    continue
                t = int(string[ind:i+k])
            else:
                t = int(string[i:i+k])
            if num % t == 0:
                res += 1
        return res
    
# source:https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/description/
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = []
        temp = 0
        for v in nums:
            if not v:
                count.append(temp)
                temp = 0
            else:
                temp += 1
        count.append(temp)

        mx = 0
        if len(count) == 1:
            return len(nums) - 1
        
        for i in range(len(count)-1):
            mx = max(mx, count[i] + count[i+1])

        return mx