# source:https://leetcode.cn/problems/maximum-good-subarray-sum/ 前缀和+Hashtable
from cmath import inf
from collections import defaultdict
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        sign = defaultdict(bool)
        total = 0
        ans = -inf
        for i, v in enumerate(nums):
            total += nums[i]
            if sign[v-k]:
                ans = max(total - d[v-k], ans)
            if sign[v+k]:
                ans = max(total - d[v+k], ans)
            if sign[v]:
                d[v] = min(d[v], total - v)
            else:
                d[v] = total - v
            sign[v] = True
        return ans if ans != -inf else 0

# source:https://leetcode.cn/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/ 前缀和+二分+滑窗
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        ans = []
        i = 0
        total = 0
        res = inf
        for j, v in enumerate(arr):
            total += v
            while total > target and i <= j:
                total -= arr[i]
                i += 1
            if total == target:
                ans.append([i, j])
        
        suf = [inf for _ in range(len(ans)+1)]
        for i in range(len(ans)-1,-1,-1):
            suf[i] = min(suf[i+1], ans[i][1] - ans[i][0]+1)
        # print(ans)
        # print(suf)

        for i in range(len(ans)-1):
            # 二分
            value = ans[i][1]
            left = i+1
            right = len(ans)
            while left < right:
                mid = (left+right)//2
                if ans[mid][0] <= value:
                    left = mid+1
                else:
                    right = mid
            # print(i, left)
            if left != len(ans):
                res = min(res, ans[i][1] - ans[i][0]+1 + suf[left])
            # print(res)
        
        return res if res != inf else -1