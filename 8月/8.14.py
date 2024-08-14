# source:https://leetcode.cn/problems/special-array-ii/description/ 二分
from collections import defaultdict
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        def fun_left(v):
            i = 0
            j = len(record)
            while i < j:
                mid = (i+j)//2
                if record[mid][0] < v:
                    i = mid + 1
                else:
                    j = mid
            return i
        
        def fun_right(v):
            i = 0
            j = len(record)
            while i < j:
                mid = (i+j)//2
                if record[mid][1] <= v:
                    i = mid+1
                else:
                    j = mid
            return i

        record = []
        for j in range(1,len(nums)):
            if nums[j]%2 == nums[j-1]%2:
                record.append([j-1, j])
        res = []
        for n,m in queries:
            left = fun_left(n)
            right = fun_right(m)
            if left < right:
                res.append(False)
            else:
                res.append(True)
        return res

# source:https://leetcode.cn/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/ 定长滑窗
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i = j = 0
        res = count = 0
        d = dict()
        while j < len(nums):
            d[nums[j]] = d.get(nums[j], 0) + 1
            count += nums[j]
            if j-i+1 == k:
                if len(d) == k:
                    res = max(res,count)
                count -= nums[i]
                d[nums[i]] -= 1
                if d[nums[i]] == 0:
                    del d[nums[i]]
                i += 1
            j += 1
        return res

# source:https://leetcode.cn/problems/find-the-longest-equal-subarray/description/ 变长滑窗
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos_list = defaultdict(list)
        for i, v in enumerate(nums):
            pos_list[v].append(i - len(pos_list[v]))
        # print(pos_list)
        res = 0
        for pos in pos_list.values():
            if len(pos) <= res:
                continue 
            i = 0
            for j, v in enumerate(pos):
                if v - pos[i] > k :
                    i += 1
                res = max(res, j - i + 1)
        return res