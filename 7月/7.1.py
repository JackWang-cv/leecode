# source:https://leetcode.cn/problems/maximum-path-quality-of-a-graph/ dfs
from cmath import inf
from collections import defaultdict
from typing import List


class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        g = defaultdict(list)
        for x, y, z in edges:
            g[x].append((y, z))
            g[y].append((x, z))

        ans = 0
        visited = {0}

        def dfs(v, time, value):
            if v == 0:
                nonlocal ans
                ans = max(ans, value)

            for v, dist in g[v]:
                if time + dist <= maxTime:
                    if v not in visited:
                        visited.add(v)
                        dfs(v, time + dist, value + values[v])
                        visited.discard(v)
                    else:
                        dfs(v, time + dist, value)

        dfs(0, 0, values[0])
        return ans

# source:https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/description/  二分


class Solution1:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        mn = inf
        i = 0
        j = len(nums)-1
        while i<=j:
            mid = (i+j)//2
            if nums[mid]<mn:
                mn = nums[mid]
            if nums[i] == nums[mid]:
                i += 1
            elif nums[j] == nums[mid]:
                j -= 1
            elif nums[i] < nums[mid]:
                if nums[mid] < nums[j]:
                    j = mid-1
                else:
                    i = mid+1
            else:
                if nums[mid] < nums[j]:
                    j = mid-1
                else:
                    i = mid+1
        return mn