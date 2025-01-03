# source:https://leetcode.cn/problems/smallest-range-i/ 贪心
from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        dif = nums[-1] - nums[0]
        if dif <= 2*k:
            return 0
        else:
            return dif - 2*k

# source:https://leetcode.cn/problems/smallest-range-ii/description/
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1] - nums[0]
        for i, v in enumerate(nums):
            if i == len(nums)-1:
                break
            mx = max(nums[-1]-k, nums[i]+k)
            mn = min(nums[0]+k, nums[i+1]-k)
            ans = min(ans, mx-mn)
        return ans