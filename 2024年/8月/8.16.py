# source: https://leetcode.cn/problems/minimum-swaps-to-group-all-1s-together-ii/ 滑窗
from cmath import inf
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_one = 0
        for v in nums:
            if v:
                total_one += 1

        res = inf
        i = j = count = 0
        while i < len(nums):
            if nums[j % len(nums)]:
                count += 1
            if j-i+1 > total_one:
                if nums[i]:
                    count -= 1
                i += 1
            if j-i+1 == total_one:
                res = min(res, total_one-count)
            j += 1
        return res

# source:https://leetcode.cn/problems/rotate-image/ 
from collections import deque
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i = len(matrix)-1
        j = 0
        t = 0
        q = deque()
        while i > j:
            total = 2*(i-j+1) + 2*(i-j-1)
            for _ in range(total):
                if j == t and i > t:
                    q.append(matrix[i][j])
                    i -= 1
                elif j < len(matrix)-1-t and i == t:
                    q.append(matrix[i][j])
                    j += 1
                elif j == len(matrix)-1-t and i < len(matrix)-1-t:
                    q.append(matrix[i][j])
                    i += 1
                elif j > t and i == len(matrix)-t-1:
                    q.append(matrix[i][j])
                    j -= 1
            
            i = j = t
            for _ in range(total):
                if j == t and i > t:
                    matrix[i][j] = q.popleft()
                    i -= 1
                elif j < len(matrix)-1-t and i == t:
                    matrix[i][j] = q.popleft()
                    j += 1
                elif j == len(matrix)-1-t and i < len(matrix)-1-t:
                    matrix[i][j] = q.popleft()
                    i += 1
                elif j > t and i == len(matrix)-t-1:
                    matrix[i][j] = q.popleft()
                    j -= 1
            
            t += 1
            i = len(matrix) - 1 - t
            j = t