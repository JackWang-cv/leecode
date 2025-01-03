# source:https://leetcode.cn/problems/maximum-sum-of-almost-unique-subarray/description/
from cmath import inf
from collections import Counter
from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        i = j = 0
        d = {}
        res = count = 0
        while j < len(nums):
            count += nums[j]
            d[nums[j]] = d.get(nums[j],0) + 1
            if j-i == k:
                count -= nums[i]
                d[nums[i]] -= 1
                if d[nums[i]] == 0:
                    del d[nums[i]]
                i += 1
            if j - i + 1 == k:
                if len(d) >= m :
                    res = max(res, count)
            j += 1
        return res

# source:https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right/description/
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        d = Counter(s)
        if len(d) < 3:
            if not k:
                return 0
            return -1
        i = 0
        res = inf
        my_d = {}
        for j, v in enumerate(s):
            my_d[v] = my_d.get(v, 0) + 1
            while ((d['a'] - my_d.get('a', 0) < k) or (d['b'] - my_d.get('b', 0) < k) or (d['c'] - my_d.get('c', 0) < k)) and i <= j:
                my_d[s[i]] -= 1
                if my_d[s[i]] == 0:
                    del my_d[s[i]]
                i += 1
            if (d['a'] - my_d.get('a', 0) >= k) and (d['b'] - my_d.get('b', 0) >= k) and (d['c'] - my_d.get('c', 0) >= k):
                res = min(res, len(s) - (j-i+1))
        return res if res != inf else -1
            