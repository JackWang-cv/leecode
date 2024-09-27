# source:https://leetcode.cn/problems/number-of-bit-changes-to-make-two-integers-equal/description/
from collections import defaultdict
from typing import List


class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n | k != n:
            return -1
        
        ans = n ^ k
        i = count = 0
        while (1 << i) <= ans:

            if (1 << i) | ans == ans:
                count += 1
            i += 1
        return count

# source:https://leetcode.cn/problems/sort-integers-by-the-number-of-1-bits/description/
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = defaultdict(list)
        for i, v in enumerate(arr):
            d[v.bit_count()].append(v)
        ans = []
        for i, Arr in sorted(d.items(), key = lambda x:x[0]):
            ans += sorted(Arr)
        return ans

# source:https://leetcode.cn/problems/minimum-bit-flips-to-convert-number/description/
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()