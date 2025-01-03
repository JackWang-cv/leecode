# source: https://leetcode.cn/problems/convert-to-base-2/description/

# +2+1 = +4-2+1
class Solution:
    def baseNeg2(self, n: int) -> str:
        res = n
        for i in range(1, 30, 2):
            if res >> i & 1:
                res += 1 << (i + 1)
        return bin(res)[2:]
