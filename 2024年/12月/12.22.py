import heapq
import math
# source:https://leetcode.cn/problems/sort-integers-by-the-power-value/ 堆
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        store = []
        heapq.heapify(store)
        for i, v in enumerate(list(range(lo, hi+1))):
            cnt = 0
            temp = math.log(v, 2)
            if temp == int(temp):
                cnt += int(temp)
                heapq.heappush(store, [cnt, i])
                continue
            while temp != int(temp):
                v = v*3+1 if v % 2 else v//2
                temp = math.log(v, 2)
                cnt += 1
            cnt += int(temp)
            heapq.heappush(store, [cnt, i])

        for _ in range(k):
            num, index = heapq.heappop(store)
        return lo+index
                
# source:https://leetcode.cn/u/mo-wu-jie-li/ 二分 文字游戏
class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def find(value):
            mn = inf
            for i in range(len(composition)):
                total = 0
                for index, v in enumerate(composition[i]):
                    sub = v*value - stock[index]
                    if sub > 0:
                        total += sub*cost[index]
                mn = min(mn, total)
            return mn <= budget
        
        i, j = 0, budget+max(stock)
        while i < j:
            mid = (i+j+1)//2
            if find(mid):
                i = mid
            else:
                j = mid-1
        return i
