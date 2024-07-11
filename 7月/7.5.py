# source:https://leetcode.cn/problems/search-a-2d-matrix-ii/description/ 二分
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            t = matrix[i]
            i = 0
            j = len(t)-1
            while i<=j:
                mid = (i+j)//2
                if t[mid] == target:
                    return True
                elif t[mid] > target:
                    j = mid-1
                else:
                    i = mid+1
        return False

