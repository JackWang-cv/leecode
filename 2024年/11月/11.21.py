# source:https://leetcode.cn/problems/house-robber/ dp 记忆化搜索
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        store = [-1] * n
        def dfs(i):
            if i < 0:
                return 0
            if store[i] != -1:
                return store[i]
            res = max(dfs(i-1), dfs(i-2) + nums[i])
            store[i] = res
            return res
        return dfs(n-1)

# source:https://leetcode.cn/problems/house-robber-ii/ dp 空间复杂度优化为O(1)
class Solution:
    def rob1(self, nums):
        f0, f1 = 0, 0
        for i, v in enumerate(nums):
            f0, f1 = f1, max(f1, f0+v)
        return f1
    def rob(self, nums: List[int]) -> int:
        return max(nums[0]+self.rob1(nums[2:-1]), self.rob1(nums[1:]))

# source:https://leetcode.cn/problems/minimum-operations-to-halve-array-sum/ 堆
import heapq
from typing import Counter, List
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        ori = 0
        for i in range(len(nums)):
            ori += nums[i]
            nums[i] = -1*nums[i]
        ans,res = 0, ori
        heapq.heapify(nums)
        while 1:
            temp = heapq.heappop(nums)
            ori -= (-1*temp)/2
            ans += 1
            if ori <= res/2:
                return ans
            else:
                heapq.heappush(nums, temp/2)

# source:https://leetcode.cn/problems/maximum-product-after-k-increments/ 堆
import heapq
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = pow(10, 9)+7
        heapq.heapify(nums)
        for _ in range(k):
            temp = heapq.heappop(nums)
            heapq.heappush(nums, temp+1)
        ans = 1
        for v in nums:
            ans *= v
            if ans > MOD:
                ans %= MOD
        return ans

# source:https://leetcode.cn/problems/delete-and-earn/ dp
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dic = Counter(nums)
        L = sorted(dic.keys())
        n = len(L)
        store = [-1] * n 
        def dfs(i):
            if i < 0:
                return 0
            if store[i] != -1:
                return store[i]
            k = 1
            while i-k >= 0:
                if L[i-k] != L[i]-1:
                    break
                k += 1
            res = max(dfs(i-1), dfs(i-k) + L[i]*dic[L[i]])
            store[i] = res
            return res
        return dfs(n-1)