# source:https://leetcode.cn/submissions/detail/575581158/ 
from collections import Counter
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        matrix = [[0 for _ in range(len(points))] for _ in range(len(points))]
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                matrix[i][j] = (x2-x1)**2 + (y2-y1)**2
                matrix[j][i] = matrix[i][j]
        ans = 0
        for i in range(len(matrix)):
            d = Counter(matrix[i])
            for k in d.keys():
                ans += d[k]*(d[k]-1)
        return ans

# source:https://leetcode.cn/problems/count-vowel-strings-in-ranges/ 前缀和
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        total = [0 for _ in range(len(words)+1)]
        store = ['a', 'e', 'i', 'o', 'u']
        for i, v in enumerate(words):
            if v[0] in store and v[-1] in store:
                p = 1
            else:
                p = 0
            total[i+1] = total[i] + p
        ans = []
        for i, j in queries:
            ans.append(total[j+1] - total[i])
        return ans

# source:https://leetcode.cn/problems/longest-subsequence-with-limited-sum/ 后缀+二分
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        total = sum(nums)
        temp = sorted(nums)
        suf = [total for _ in range(len(nums)+1)]
        for i in range(len(nums)-1, -1, -1):
            suf[i] = suf[i+1] - temp[i]
        def find(value):
            i = 0
            j = len(suf)
            while i < j:
                mid = (i + j)//2
                if suf[mid] > value:
                    j = mid
                else:
                    i = mid+1
            return i
        for v in queries:
            ans.append(find(v)-1)
        return ans