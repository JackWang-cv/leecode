# source:https://leetcode.cn/problems/minimize-xor/
from typing import List


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n = num2.bit_count()
        n1 = num1.bit_count()
        i = 0
        if n > n1:
            while num1.bit_count() < n :
                num1 |= (1 << i)
                i += 1
        elif n < n1:
            count = 0
            while count < n1 - n:
                if (num1 >> i) & 1:
                    num1 ^= (1 << i)
                    count += 1
                i += 1 
        return num1

# source: https://leetcode.cn/problems/find-xor-beauty-of-array/description/ 如何推导的
class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        ans = 0
        for v in nums:
            ans ^= v
        return ans

# source:https://leetcode.cn/problems/maximum-xor-after-operations/ 如何推导
class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        temp = 0
        for v in nums:
            temp |= v
        return temp