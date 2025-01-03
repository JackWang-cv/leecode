# source:https://leetcode.cn/problems/minimum-number-of-days-to-make-m-bouquets/description/ 二分
from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(v):
            count = 0
            for i in bloomDay:
                visit.append(i<=v)
            temp = 0
            for i in range(len(visit)):
                if not visit[i]:
                    temp = 0
                if temp < k and visit[i]:
                    temp += 1
                if k == temp:
                    temp = 0
                    count += 1
            return count < m
        if len(bloomDay) < m*k:
            return -1
        i = min(bloomDay)
        j = max(bloomDay)
        visit = []
        while i<j:
            mid = (i+j)//2
            visit.clear()
            if check(mid):
                i = mid+1
            else:
                j = mid
        return i

# source:https://leetcode.cn/problems/find-the-value-of-the-partition/ 贪心
class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        mn = inf
        for i in range(len(nums)-1):
            j = i+1
            temp = nums[j] - nums[i]
           
            if temp < mn:
                mn = temp
        return mn