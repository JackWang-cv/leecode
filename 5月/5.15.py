# source: https://leetcode.cn/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0

        new_s = ''
        i = 0
        while s[i] == ' ':
            i += 1
            if i == len(s):
                break

        if i < len(s):
            if s[i] == '-':
                new_s += '-'
                i += 1
            elif s[i] == '+':
                i += 1

        if i < len(s):
            if s[i] == '0':
                while s[i] == '0':
                    i += 1
                    if i == len(s):
                        break

        if i < len(s):
            while (s[i] >= '0') and (s[i] <= '9'):
                new_s += s[i]
                i += 1
                if i == len(s):
                    break
        if new_s == '-' or new_s == '':
            new_s = '0'

        res = int(new_s)

        if res < pow(-2, 31):
            res = pow(-2, 31)
        elif res > (pow(2, 31) - 1):
            res = (pow(2, 31) - 1)
        return res