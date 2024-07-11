# source:https://leetcode.cn/problems/valid-perfect-square/description/ 二分
from charset_normalizer.md import List


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        i = 1
        j = num//2
        while i<=j:
            mid = (i+j)//2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                j = mid-1
            else:
                i = mid+1
        return False

# source:https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/description/ 二维二分


class Solution1:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def check(v, target) -> bool:
            num = 0
            nonlocal n
            h, j = n, 0
            while h >= 0 and j <= n:
                if matrix[h][j] <= v:
                    num += h + 1
                    j += 1
                else:
                    h -= 1
            return num >= target

        n = len(matrix) - 1
        i = matrix[0][0]
        j = matrix[n][n]
        while i < j:
            mid = (i + j) // 2
            if check(mid, k):
                j = mid
            else:
                i = mid + 1
        return i