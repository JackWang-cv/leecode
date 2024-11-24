# source:https://leetcode.cn/problems/ways-to-express-an-integer-as-sum-of-powers/ 0-1背包变形
import math
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        max_base = 1
        while max_base**x <= n:
            max_base += 1
        max_base -= 1
        row = max_base+1
        f = [[0 for _ in range(n+1)] for _ in range(2)]
        f[0][0] = 1
        MOD = pow(10,9)+7
        for i, v in enumerate(range(1, row)):
            for c in range(n+1):
                if c < pow(v, x):
                    f[(i+1)%2][c] = f[i%2][c]
                else:
                    f[(i+1)%2][c] = (f[i%2][c] + f[i%2][c - pow(v, x)]) % (MOD)
        # print(i)
        return f[(i+1)%2][-1]

# source:https://leetcode.cn/problems/find-the-substring-with-maximum-cost/ 最大子数组和 一维dp
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        
        d = defaultdict(int)
        SET = set(chars)
        for i, v in enumerate(chars):
            d[v] = vals[i]
        f1 = ord(s[0]) - 96 if s[0] not in SET else d[s[0]]
        mx = max(0, f1)
        # print(d)
        for i in range(1, len(s)):
            value = ord(s[i]) - 96 if s[i] not in SET else d[s[i]]
            f1 = max(f1+value, value)
            mx = max(mx, f1)
            # print(f1, mx)
        return mx

# source:https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/ 逆序对 归并排序
class Solution:
    def reversePairs(self, record: List[int]) -> int:
        ans = 0
        def merge(array1, array2):
            res = []
            nonlocal ans
            i, j = 0, 0
            n1, n2 = len(array1), len(array2)
            for _ in range(n1+n2):
                if i == n1:
                    res += array2[j:]
                    break
                elif j == n2:
                    res += array1[i:]
                    break
                if array1[i] <= array2[j]:
                    res.append(array1[i])
                    i += 1
                else:
                    ans += (n1 - i)
                    res.append(array2[j])
                    j += 1
            return res
        
        def merge_sort(array):
            if len(array) <= 1:
                return array
            half = len(array)//2
            left = merge_sort(array[:half])
            right = merge_sort(array[half:])

            return merge(left, right)
        
        merge_sort(record)
        return ans

# source:https://leetcode.cn/problems/longest-common-subsequence/ 最长子数列长度 dp
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        f = [[0 for _ in range(len(text1)+1)] for _ in range(2)]
        for i in range(len(text2)):
            for j in range(len(text1)):
                if text1[j] != text2[i]:
                    f[(i+1)%2][j+1] = max(f[i%2][j+1], f[(i+1)%2][j])
                else:
                    f[(i+1)%2][j+1] = f[i%2][j] + 1
        return f[(i+1)%2][-1]

# source:https://leetcode.cn/problems/edit-distance/ 编辑距离 上一题的变形
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        f = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        f[0] = list(range(len(word2)+1))
        for i in range(len(word1)):
            f[i+1][0] = i + 1
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    f[i+1][j+1] = f[i][j]
                else:
                    f[i+1][j+1] = min(f[i][j+1], min(f[i][j], f[i+1][j])) + 1
        return f[-1][-1]