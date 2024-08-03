# source:https://leetcode.cn/problems/maximum-points-inside-the-square/solutions/ 二分
from cmath import inf
from typing import List


class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        def check(v):
            count = 0
            dit = {}
            for i in range(len(points)):
                if v >= max(abs(points[i][0]), abs(points[i][1])):
                    if dit.get(s[i], 0) == 0:
                        count += 1
                        dit[s[i]] = 1
                    else:
                        return False
            nonlocal mn
            if count > mn:
                mn = count
            return True
            
        i = j = 0
        for n, m in points:
            j = max(j, max(abs(n), abs(m)))
        
        mn = 0
        while i <= j:
            mid = (i+j)//2
            if check(mid):
                i = mid+1
            else:
                j = mid-1
        return mn

# source:https://leetcode.cn/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/ 定长滑动窗口
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        mn = inf
        for i in range(len(nums)-k+1):
            mn = min(mn, nums[i]-nums[i+k-1])
        return mn

# source:https://leetcode.cn/problems/find-the-longest-semi-repetitive-substring/
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        last_s = ''
        j = 0
        visit = 1
        count = mx = 0
         
        while j < len(s):
            if s[j] != last_s:
                count += 1
            else:
                if visit:
                    visit = 0
                    count += 1          
                else:    
                    count = j - t + 1
                t = j
            last_s = s[j]    
            j += 1
            mx = max(mx, count)
        
        return mx