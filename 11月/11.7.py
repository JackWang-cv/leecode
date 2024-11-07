# source:https://leetcode.cn/submissions/detail/578803549/ 二维前缀和+二分
from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        def find(value, left, right):
            i_l, i_r = max(0, left - right), max(0, right - left)
            j_l, j_r = left, right
            # print(i_l, j_l)
            while i_l < j_l:
                mid_l = (i_l + j_l)//2
                # mid_r = mid_l + (right - left)
                mid_r = (i_r + j_r)//2
                area = value - store[mid_l][right] - store[left][mid_r] + store[mid_l][mid_r]
                if area <= threshold:
                    j_l = mid_l
                    j_r = mid_r
                else:
                    i_l = mid_l+1
                    i_r = mid_r+1
            # print(i_l, i_r, left, right, area)
            return left - i_l 
        row, col = len(mat), len(mat[0])
        store = [[0 for _ in range(col+1)] for _ in range(row+1)]
        for i in range(1, row+1):
            for j in range(1, col+1):
                store[i][j] = store[i-1][j] + store[i][j-1] - store[i-1][j-1] + mat[i-1][j-1]
        # print(store)
        ans = 0
        for i in range(1, row+1):
            for j in range(1, col+1):
                ans = max(ans, find(store[i][j], i, j))
        return ans