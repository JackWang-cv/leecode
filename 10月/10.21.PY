# 哈希表维护，使得遍历次数变少
# source:https://leetcode.cn/problems/smallest-range-ii/description/
from cmath import inf
from collections import defaultdict
from typing import List


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1] - nums[0]
        for i, v in enumerate(nums):
            if i == len(nums)-1:
                break
            mx = max(nums[i]+k, nums[-1]-k)
            mn = min(nums[0]+k, nums[i+1]-k)
            ans = min(ans, mx-mn)
        return ans

# source:https://leetcode.cn/submissions/detail/574418706/
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        c = defaultdict(int)
        for i in nums1:
            for j in nums2:
                c[i+j] += 1
        for u in nums3:
            for v in nums4:
                ans += c[-u-v]
        return ans

# source:https://leetcode.cn/problems/maximum-value-of-an-ordered-triplet-ii/
from sortedcontainers import SortedList
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        i = 0
        first = 0
        ans = 0
        inverse = SortedList(nums[::-1])
        for j, v in enumerate(nums):
            if nums[i] - nums[j] >= 0:
                if nums[i] - nums[j] >= first:
                    first = nums[i] - nums[j]
            else:
                i = j
            inverse.remove(v)
            if inverse:
                ans = max(ans, inverse[-1]*first)
        return ans 

# source:https://leetcode.cn/submissions/detail/574428813/
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        d = defaultdict(int)
        for i in hours:
            d[i % 24] += 1
        ans = 0
        for i in hours:
            red = (24 - i % 24)
            if d[red % 24]:
                if red != 24 and red!= 12:
                    ans += d[red % 24]
                else:
                    ans += d[red % 24]-1
                
            if d[i % 24] > 0:
                d[i % 24] -= 1       
        return ans

# source:https://leetcode.cn/submissions/detail/574431723/
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        sub = [-inf for _ in range(len(values)+1)]
        for j in range(len(values)-1, -1, -1):
            sub[j] = max(sub[j+1], values[j]-j)
        ans = 0
        print(sub)
        for i in range(len(values)-1):
            ans = max(values[i] + i +sub[i+1], ans)
        return ans