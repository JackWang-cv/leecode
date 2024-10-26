# source:https://leetcode.cn/problems/range-product-queries-of-powers/ 位运算+前缀和
from itertools import accumulate, pairwise
from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        l = n.bit_length()
        k = 0
        store = [1]
        while k <= l:
            if (1 << k) & n:
                store.append(1<<k)
            k += 1
        # print(store)
        for i in range(1, len(store)):
            store[i] *= store[i-1]
        # print(store)
        ans = []
        for i, j in queries:    
            ans.append((store[j+1]//store[i])%(pow(10, 9)+7))
        return ans

# source:https://leetcode.cn/problems/special-array-ii/description/
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ans = []
        s = list(accumulate((x%2 == y%2 for x, y in pairwise(nums)),initial = 0))
        # print(s)
        for i, j in queries:
            ans.append(s[i] ==s[j])
        return ans

# source:https://leetcode.cn/problems/plates-between-candles/description/  二分+前缀和
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        def find_left(value):
            i = 0
            j = len(candle)-1
            while i < j:
                mid = (i+j+1)//2
                if candle[mid] >= value:
                    j = mid-1
                else:
                    i = mid
            # print(value, i)
            return i
        
        def find_right(value):
            i = 0
            j = len(candle)
            while i < j:
                mid = (i+j)//2
                if candle[mid] <= value:
                    i = mid+1
                else:
                    j = mid
            # print(value, i)
            return i
        
        candle = [0]
        for i, v in enumerate(s):
            if v == '|':
                candle.append(i)
        store = [0 for _ in range(len(candle))]
        # print(candle)
        for i in range(2, len(candle)):
            # 是否去除重叠
            store[i] = candle[i] - candle[i-1] - 1 + store[i-1]
        # print(store)
        ans = []
        for i, j in queries:
            left = find_left(i)
            # print(left)
            right = find_right(j)
            # print(left, right)
            if left+1 == right:
                ans.append(0)
            else:
                ans.append(store[right-1] - store[left+1])
        return ans