# source: https://leetcode.cn/problems/roman-to-integer/ 把规则制定好就行，hash表

# source: https://leetcode.cn/problems/roman-to-integer/
class Solution:
    def judge_I(self, s, i, j):
        if i < len(s):
            if s[i] == "I":
                i, j = self.judge_I(s, i + 1, j + 1)
            elif s[i] == "V":
                return i + 1, 4
            elif s[i] == "X":
                return i + 1, 9
        return i, j

    def judge_X(self, s, i, j):
        if i < len(s):
            if s[i] == "X":
                i, j = self.judge_X(s, i + 1, j + 10)
            elif s[i] == "L":
                return i + 1, 40
            elif s[i] == "C":
                return i + 1, 90
        return i, j

    def judge_C(self, s, i, j):
        if i < len(s):
            if s[i] == "C":
                i, j = self.judge_C(s, i + 1, j + 100)
            elif s[i] == "D":
                return i + 1, 400
            elif s[i] == "M":
                return i + 1, 900
        return i, j

    def judge_V(self, s, i, j):
        if i < len(s):
            if s[i] == "I":
                i, j = self.judge_V(s, i + 1, j + 1)
        return i, j

    def judge_L(self, s, i, j):
        if i < len(s):
            if s[i] == "X":
                i, j = self.judge_L(s, i + 1, j + 10)
        return i, j

    def judge_D(self, s, i, j):
        if i < len(s):
            if s[i] == "C":
                i, j = self.judge_D(s, i + 1, j + 100)
        return i, j

    def judge_M(self, s, i, j):
        if i < len(s):
            if s[i] == "M":
                i, j = self.judge_M(s, i + 1, j + 1000)
        return i, j

    def romanToInt(self, s: str) -> int:
        res = 0
        i = 0

        while i < len(s):
            if s[i] == "I":
                i, t = self.judge_I(s, i + 1, 1)
            elif s[i] == "X":
                i, t = self.judge_X(s, i + 1, 10)
            elif s[i] == "C":
                i, t = self.judge_C(s, i + 1, 100)
            elif s[i] == "V":
                i, t = self.judge_V(s, i + 1, 5)
            elif s[i] == "L":
                print(s)
                i, t = self.judge_L(s, i + 1, 50)
            elif s[i] == "D":
                i, t = self.judge_D(s, i + 1, 500)
            elif s[i] == "M":
                i, t = self.judge_M(s, i + 1, 1000)

            res += t
        return res


