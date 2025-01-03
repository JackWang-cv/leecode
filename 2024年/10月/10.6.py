# source：https://leetcode.cn/problems/gas-station/ 贪心
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n:
            sum_of_gas = sum_of_cost = 0
            cnt = 0
            while cnt < n:
                j = (i + cnt) % n
                sum_of_gas += gas[j]
                sum_of_cost += cost[j]
                if sum_of_cost > sum_of_gas:
                    break
                cnt += 1
            if cnt == n:
                return i
            else:
                i += cnt + 1
        return -1

# source:https://leetcode.cn/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/description/
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        for v in nums:
            ans ^= v
        ans ^= k
        return ans.bit_count()

# source:https://leetcode.cn/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/description/ 
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        store = [0]
        temp = 0
        count = 0
        for v in arr:
            temp ^= v
            store.append(temp)
        
        def dfs(temp, cnt):
            nonlocal count
            if cnt == 2:
                i, k = temp
                if store[i] == store[k+1]:
                    count += k-i
                return 
            if cnt == 0:
                for i in range(len(arr)-1):
                    dfs([i], 1)
            else:
                for k in range(temp[-1]+1, len(arr)):
                    dfs(temp+[k], 2)
        dfs([], 0)

        return count