# source:https://leetcode.cn/submissions/detail/577564739/ 二维前缀和
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        total = [[0 for _ in range(len(mat)+1)] for _ in range(len(mat[0]))]
        for n in range(len(mat[0])):
            for m in range(len(mat)):
                total[n][m+1] = total[n][m] + mat[m][n]
        # print(total)
        ans = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                left = max(j - k, 0)
                right = min(j + k, len(mat[0])-1)
                top = max(i - k, 0)
                bottom = min(i + k + 1, len(mat))
                temp = 0
                # print(i, j)
                # print(left, right, top, bottom)
                for index in range(left, right+1):
                    temp += total[index][bottom] - total[index][top]
                ans[i][j] = temp
        return ans