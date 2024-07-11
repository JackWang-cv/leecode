# source:https://leetcode.cn/problems/separate-black-and-white-balls/


class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0
        i = 0
        j = len(s ) -1
        ls = list(s)
        if j== 0:
            return 0

        k = k1 = 1
        while i + 1 < j:
            if ls[i] > ls[i + 1]:
                res += k
                t = i - k
                if t < 0:
                    t = 0
                ls[t:i + 2] = list(ls[i + 1]) + ls[t:i + 1]
            elif ls[i] == ls[i + 1] and ls[i] == '1':
                k += 1
            i += 1

            if i + 1 >= j:
                break

            if ls[j] < ls[j - 1]:
                res += k1
                ls[j - 1:j + k + 1] = ls[j:j + k + 1] + list(ls[j - 1])
            elif ls[j] == ls[j - 1] and ls[j] == '0':
                k1 += 1

            j -= 1
        if ls[i] > ls[j]:
            res += k * k1
        return res

# 不会超市
class Solution1:
    def minimumSteps(self, s):
        ans, sum = 0, 0
        for i in range(len(s)):
            if s[i] == '1':
                sum += 1
            else:
                ans += sum
        return ans

