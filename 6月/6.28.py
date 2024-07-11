# source:https://leetcode.cn/problems/search-a-2d-matrix/description/ 二分
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix)*len(matrix[0])-1
        while i<=j:
            mid = (i+j)//2
            row = mid // len(matrix[0])
            column = mid % len(matrix[0])
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] > target:
                j = mid-1
            else:
                i = mid+1
        return False