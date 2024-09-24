# source:https://leetcode.cn/problems/number-of-even-and-odd-bits/description/ 位运算
from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        i = 0
        answer = [0, 0]
        while n > 0:
            n >>= i if i < 1 else 1
            if n & 1:
                answer[i % 2] += 1
            i += 1
        return answer
    
# source:https://leetcode.cn/problems/maximize-number-of-subsequences-in-a-string/ 贪心 前缀和
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        count = 0
        if pattern[0] == pattern[1]:
            for i in range(len(text)):
                if text[i] == pattern[0]:
                    count += 1
        
            return (1+count)*count//2
        
        a = []
        count1 = count2 = 0
        for i in range(len(text)-1, -1, -1):
            if text[i] == pattern[1]:
                count += 1
            elif text[i] == pattern[0]:
                count1 += count
        count1 += count
        count -= count
        for j in range(len(text)):
            if text[j] == pattern[0]:
                count += 1
            elif text[j] == pattern[1]:
                count2 += count
        count2 += count
        return max(count1, count2)

# source:https://leetcode.cn/problems/power-of-two/description/ 计算1的个数
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
