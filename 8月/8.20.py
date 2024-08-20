from typing import List
from sortedcontainers import SortedList
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        res = 0
        i = j = 0
        temp = SortedList()
        while j < len(nums):
            temp.add(nums[j])
            t1 = abs(temp[-1] - nums[j])
            t2 = abs(temp[0] - nums[j])
            while t1 < 0 or t1 > 2 or t2 < 0 or t2 > 2 and i <= j:
                print(temp)
                
                temp.remove(nums[i])
                t1 = abs(temp[-1] - nums[j])
                t2 = abs(temp[0] - nums[j])
                i += 1 
            res += j-i+1
            j += 1
        return res

X = Solution()
X.continuousSubarrays([42,41,42,41,41,40,39,38])