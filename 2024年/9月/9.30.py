# source:https://leetcode.cn/problems/check-if-bitwise-or-has-trailing-zeros/description/
from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        count = 0
        for v in nums:
            if not (v & 1):
                count += 1
        return False if count < 2 else True

# source:https://leetcode.cn/problems/seat-reservation-manager/ heap
from sortedcontainers import SortedList
class SeatManager:

    def __init__(self, n: int):
        self.so = SortedList([i for i in range(1, n+1)])
    def reserve(self) -> int:
        
        mn = self.so[0]
        self.so.remove(mn)
        return mn

    def unreserve(self, seatNumber: int) -> None:
        self.so.add(seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

# source:https://leetcode.cn/problems/minimum-flips-to-make-a-or-b-equal-to-c/
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        t = (a | b) ^ c
        ans = i = 0
        while (t >> i) > 0:
            if (t >> i) & 1:
                if (c >> i) & 1:
                    ans += 1
                else:
                    if (a >> i) & 1:
                        ans += 1
                    if (b >> i) & 1:
                        ans += 1
            i += 1
        return ans

# source:https://leetcode.cn/problems/longest-subarray-with-maximum-bitwise-and/description/
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = i = 0
        mx = -1
        for j, v in enumerate(nums):
            if v == nums[i] and mx <= v:
                mx = v
                ans = max(ans, j-i+1)
            else:
                if mx < v:
                    mx = v
                    ans = 1
                i = j
        return ans