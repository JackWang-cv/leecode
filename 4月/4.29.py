# source:https://leetcode.cn/problems/sort-the-matrix-diagonally/

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat[0])
        n = len(mat)
        for i in range(min(m, n)):
            for j in range(n-i-1):
                for k in range(m-i-1):
                    if(mat[j][k]>mat[j+1][k+1]):
                        mat[j][k], mat[j+1][k+1] = mat[j+1][k+1], mat[j][k]
        return mat