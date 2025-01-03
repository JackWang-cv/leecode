# source:https://leetcode.cn/problems/heaters/ 7.26 二刷
from bisect import bisect_left, bisect_right
from typing import Counter, List
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def find(value):
            former = 0
            for v in heaters:
                left = v - value
                right = v + value
                l = bisect_left(houses, left)
                r = bisect_right(houses, right)
                if l - former >= 1:
                    return False
                former = r
            if r < len(houses):
                return False
            return True

        houses.sort()
        heaters.sort()
        i, j = 0, 10**9
        while i < j:
            mid = (i+j)//2
            if find(mid):
                j = mid
            else:
                i = mid+1
        return i

# source:https://leetcode.cn/problems/minimum-time-to-repair-cars/ 二分
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def find(time):
            cnt = 0
            for r, m in c.items():
                cnt += m*int(pow((time // r), 0.5))
            return cnt >= cars
        
        c = Counter(ranks)
        i, j = 1, (cars**2)*max(ranks)
        while i < j:
            mid = (i+j)//2
            if find(mid):
                j = mid
            else:
                i = mid+1
        return i