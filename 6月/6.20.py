# source:https://leetcode.cn/problems/number-of-beautiful-pairs/
from typing import List


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        res = 0
        cnt = [0] * 10
        for x in nums:
            for y in range(1, 10):
                if gcd(x % 10, y) == 1:
                    res += cnt[y]
            while x >= 10:
                x //= 10
            cnt[x] += 1
        return res