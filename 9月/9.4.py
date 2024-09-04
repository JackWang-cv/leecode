# source:https://leetcode.cn/problems/online-stock-span/ 单调栈
from typing import List


class StockSpanner:

    def __init__(self):
        self.stack = list()

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append([price,1])
            return 1
        else:
            ans = 1
            while self.stack:
                if self.stack[-1][0] > price:
                    self.stack.append([price, ans])
                    return ans
                else:
                    t = self.stack.pop()
                    ans += t[1]
            self.stack.append([price, ans])
            return ans

# source:https://leetcode.cn/problems/longest-well-performing-interval/description/
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        s = [0] * (len(hours)+1)
        st = [0]
        for i, v in enumerate(hours, 1):
            s[i] = s[i-1] + (1 if v > 8 else -1)
            if s[i] < s[st[-1]]:
                st.append(i)
        ans = 0
        for i in range(len(hours), 0, -1):
            while st and s[i] > s[st[-1]]:
                ans = max(ans, i - st.pop())
        return ans
            