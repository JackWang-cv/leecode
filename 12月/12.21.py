# source:https://leetcode.cn/problems/sort-the-students-by-their-kth-score/ 堆
import heapq
from typing import List


class Solution: 
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        store = []
        for i, score_ in enumerate(score):
            store.append([-1*score_[k], i])
        heapq.heapify(store)
        while store:
            _, index = heapq.heappop(store)
            ans.append(score[index])
        return ans

# source:https://leetcode.cn/problems/maximum-value-at-a-given-index-in-a-bounded-array/submissions/588469065/ 二刷 12.21 一刷 7.30
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def judge(value):
            total = 0
            if value - index > 0:
                total += (value-index + value-1)*index//2
            else:
                total += 1*(index-value+1)+(1 + value-1)*(value-1)//2

            if n - index <= value:
                total += (value + value - (n-index-1))*(n-index)//2
            else:
                total += (value + 1)*(value)//2 + 1*(n-index-value)
            
            return total > maxSum
  
        i, j = 1, maxSum
        while i < j:
            mid = (i+j+1)//2
            if judge(mid):
                j = mid-1
            else:
                i = mid
            # print(f'{i = } {mid = }')
        return i

# source:https://leetcode.cn/problems/furthest-building-you-can-reach/submissions/588472196/ 二刷 一刷：7.31
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:       
        def judge(value):
            store = []
            heapq.heapify(store)
            res = 0
            for i in range(1, value+1):
                if heights[i]-heights[i-1]>0:
                    heapq.heappush(store, heights[i]-heights[i-1])
            for _ in range(len(store)-ladders):
                res += heapq.heappop(store)
            return res <= bricks
        i, j = 0, len(heights)-1
        while i < j:
            mid = (i+j+1)//2
            if judge(mid):
                i = mid
            else:
                j = mid-1
        return i