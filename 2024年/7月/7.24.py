# source:https://leetcode.cn/problems/relocate-marbles/ hashtable 并不是并查集
from typing import List


class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        mp = {}
        ans = []
        for num in nums:
            mp[num] = True
        for i in range(len(moveFrom)):
            if moveFrom[i] in mp:
                del mp[moveFrom[i]]
            mp[moveTo[i]] = True
        ans = list(mp.keys())
        ans.sort()
        return ans

# source: https://leetcode.cn/problems/count-the-number-of-fair-pairs/description/ 二分
class Solution1:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def find(i, j, v):
            while i < j:
                mid = (i + j) // 2
                if nums[mid] >= v:
                    j = mid
                else:
                    i = mid + 1
            return i

        def find1(i, j, v):
            while i < j:
                mid = (i + j) // 2
                if nums[mid] <= v:
                    i = mid + 1
                else:
                    j = mid
            return i

        nums.sort()
        count = 0
        for i in range(len(nums) - 1):
            temp = nums[i]
            left = i + 1
            right = len(nums)
            t1 = find(left, right, lower - temp)
            t2 = find1(left, right, upper - temp)
            count += (t2 - t1) if t2 - t1 > 0 else 0
        return count

# source:https://leetcode.cn/problems/minimum-time-to-complete-trips/description/ 二分
class Solution2:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        i = 1
        j = min(time)*totalTrips
        while i<j:
            mid = (i+j)//2
            c = 0
            for t in time:
                c += mid // t
            if c >= totalTrips:
                j = mid
            else:
                i = mid+1
        return i

# source: https://leetcode.cn/problems/minimum-speed-to-arrive-on-time/description/
class Solution4:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        i = 1
        j = 10 ** 7 + 1
        while i < j:
            mid = (i + j) // 2
            res = 0
            for d in range(len(dist)):
                t1 = dist[d] / mid
                t2 = dist[d] // mid
                if d == len(dist) - 1:
                    res += t1
                    break
                res += t2 + 1 if t1 != t2 else t2

            if res <= hour:
                j = mid
            else:
                i = mid + 1
        return i if i != 10 ** 7 + 1 else -1
