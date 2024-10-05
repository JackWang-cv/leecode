# source:https://leetcode.cn/problems/xor-queries-of-a-subarray/description/
from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre = [0]
        for v in arr:
            pre.append(pre[-1] ^ v)
        ans = []
        for i, j in queries:
            ans.append(pre[j+1] ^ pre[i])
        return ans 

# source:https://leetcode.cn/problems/airplane-seat-assignment-probability/description/ 数学归纳法
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1.0 if n == 1 else 0.5

# source:https://leetcode.cn/problems/find-the-original-array-of-prefix-xor/description/
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]
        pre = pref[0]
        for i in range(1, len(pref)):
            t = pre^pref[i]
            ans.append(t)
            pre ^= t
        return ans

