# source:https://leetcode.cn/problems/final-array-state-after-k-multiplication-operations-i/ 堆
import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        store = []
        for i, v in enumerate(nums):
            store.append([v, i])
        heapq.heapify(store)
        for _ in range(k):
            value, index = heapq.heappop(store)
            heapq.heappush(store, [value*multiplier, index])
        # print(store)
        ans = [0 for _ in range(len(nums))]
        while store:
            v, index = store.pop()
            ans[index] = v
        return ans

# source:https://leetcode.cn/problems/final-array-state-after-k-multiplication-operations-ii/ 幂快速运算 堆
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        MOD = 10**9 + 7
        store = []
        for i, v in enumerate(nums):
            store.append([v, i])
        heapq.heapify(store)
        i = 0
        while i < k:
            value, index = heapq.heappop(store)
            if store == []:
                num = k - i
            else:
                v_mn, index_mn = heapq.heappop(store)
                num = min(k-i, v_mn // (value * multiplier))
                heapq.heappush(store, [v_mn, index_mn])
            inc = max(num, 1)
            i += inc
            
            # 快速幂计算 multiplier^inc
            base = multiplier
            res = 1
            while inc:
                if inc & 1:
                    res = (res * base) % MOD
                base = (base * base) % MOD
                inc >>= 1
                
            value = (value * res) % MOD
            heapq.heappush(store, [value, index])
            
        ans = [0] * len(nums)
        while store:
            v, index = heapq.heappop(store)
            ans[index] = v
        return ans

# source:https://leetcode.cn/problems/powx-n/ 快速幂
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        i, res = 0, 1
        if n < 0:
            x = 1/x
            n = -1*n
        while (n>>i):
            if (n>>i) & 1:
                res *= pow(x, 2**i)
            i += 1
        return res

# source:https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-ii/ 堆
import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        heapq.heapify(nums)
        while 1:
            mn1 = heapq.heappop(nums)
            if mn1 >= k:
                break
            if not nums:
                break
            mn2 = heapq.heappop(nums)
            heapq.heappush(nums, min(mn1, mn2)*2 + max(mn1, mn2))
            ans += 1
        return ans