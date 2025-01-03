# source:https://leetcode.cn/problems/semi-ordered-permutation/ https://leetcode.cn/problems/semi-ordered-permutation/
from collections import defaultdict
from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        ind1 = nums.index(1)
        ind2 = nums.index(len(nums))
        if ind1 < ind2:
            return ind1 + len(nums) - 1 - ind2
        else:
            return ind1 + len(nums) - 1 - ind2 - 1

# source:https://leetcode.cn/problems/smallest-string-with-swaps/ 并查集
class Union:
    def __init__(self, n):
        self.f = list(range(n))
    def find(self, x):
        if self.f[x] == x:
            return x
        else:
            self.f[x] = self.find(self.f[x])
            return self.f[x]
    def union(self, x, y):
        self.f[self.find(self.f[x])] = self.find(self.f[y])

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        ans = ['' for _ in range(len(s))]
        uf = Union(len(s))
        for i, j in pairs:
            uf.union(i, j)
        d = defaultdict(list)
        d1 = defaultdict(list)
        for i in range(len(s)):
            d[uf.find(i)].append(i)
            d1[uf.find(i)].append(s[i])
        for k in d.keys():
            d[k] = sorted(d[k])
            d1[k] = sorted(d1[k])
        for list1, list2 in zip(d.values(), d1.values()):
            for i, ind in enumerate(list1):
                ans[ind] = list2[i]
        return ''.join(ans)