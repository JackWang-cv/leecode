# source:https://leetcode.cn/problems/time-needed-to-buy-tickets/description/
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = tickets[k]
        for i, v in enumerate(tickets):
            if i < k:
                if v > tickets[k]:
                    ans += tickets[k]
                else:
                    ans += v
            elif i > k:
                if v >= tickets[k]:
                    ans += tickets[k]-1
                else:
                    ans += v
        return ans

# source:https://leetcode.cn/problems/binary-gap/description/ 位运算
class Solution:
    def binaryGap(self, n: int) -> int:
        ans = i = count = 0
        flag = 0
        while (n >> i) > 0:
            if (n >> i) & 1:
                if flag:
                    ans = max(ans, count)
                    count = 0
                else:
                    flag = 1
            if flag:
                count += 1
            i += 1
        return ans

# source:https://leetcode.cn/problems/generate-binary-strings-without-adjacent-zeros/description/ dfs
class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def dfs(s, length):
            if length == n:
                ans.append(s)
                return
            if s and s[-1] == '0':
                dfs(s + '1', length+1)
            else:
                for i in ['0', '1']:
                    dfs(s + i, length+1)
        dfs('', 0)
        return ans

# source:https://leetcode.cn/problems/find-the-k-or-of-an-array/description/
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        t = max(nums)
        i = 0
        legal = []
        while t >> i:
            count = 0
            for v in nums:
                if (v >> i) & 1:
                    count += 1
            if count >= k:
                legal.append(i)
            i += 1
        return sum([pow(2, i) for i in legal])

# source:https://leetcode.cn/problems/binary-number-with-alternating-bits/description/
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        i = 1
        last = n & 1
        while n >> i:
            t = (n >> i) & 1
            if t != last:
                last = t
            else:
                return False
            i += 1
        return True 
