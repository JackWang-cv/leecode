# source:https://leetcode.cn/problems/minimum-number-of-operations-to-make-word-k-periodic/description/
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        d = {}
        for i in range(0, len(word)-k+1, k):
            d[word[i:i+k]] = d.get(word[i:i+k], 0) + 1
        res = 0
        t = sorted(d.items(), key=lambda x:x[1])
        for i in range(len(t)-1):
            res += t[i][1]
        return res

# source:https://leetcode.cn/problems/sliding-subarray-beauty/description/
from typing import List
from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        t = SortedList()
        i = 0
        res = []
        for j, v in enumerate(nums):
            t.add(v)
            if j-i+1 > k:
                t.remove(nums[i])
                i += 1
            if j-i+1 == k:
                if t[x-1] < 0:
                    res.append(t[x-1])
                else:
                    res.append(0)
        return res

class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        res = self.countAndSay(n-1)
        i = 0
        new_res = ''
        j = 0
        while j < len(res):
            last = res[i]
            while j < len(res) and last == res[j] :
                j += 1
            temp = (j-i)
            new_res += str(temp)+res[i]
            i = j 
        return new_res