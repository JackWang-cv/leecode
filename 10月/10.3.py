# source: 贪心 + 前缀和
from typing import List


class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        suf = [0]*(n+1)
        for i in range(n-1, 0, -1):
            suf[i] = suf[i+1] | nums[i]
        ans = pre = 0
        for i, x in enumerate(nums):
            ans = max(ans, pre | x << k | suf[i+1])
            pre |= x
        return ans

# source:https://leetcode.cn/problems/minimum-array-end/description/  
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        l = pow(2, x.bit_length() - x.bit_count())
        n -= 1
        i = 0
        store = []
        while (x >> i):
            if not (x >> i) & 1:
                store.append(1 << i)
            i += 1
        ans = x
        i -= i
        if n >= l:
            while n >= l:
                n -= max(l, 1)
                i += 1
            ans = (i << x.bit_length()) | x

        if n > 0:
            temp = bin(n)[2:]
            k = count = 0
            for i in range(len(temp)-1, -1, -1):
                if temp[i] == '1':
                    count += store[k]
                k += 1
            ans |= count
        
        return ans
# 2 3 6 7