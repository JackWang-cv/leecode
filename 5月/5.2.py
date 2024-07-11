#source: https://leetcode.cn/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        t = list(str(x))
        flag = False
        res = ''
        if t[0] == '-':
            flag = True
            t = t[1:]
        for i in range(len(t)):
            res += t[len(t)-i-1]
        if flag:
            res = '-' + res
        if (int(res) > (pow(2,31)-1)) or (int(res) < (-1 * pow(2,31))):
            return 0
        else:
            return int(res)
