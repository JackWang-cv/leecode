# source:https://leetcode.cn/problems/find-the-longest-equal-subarray/description/ 滑动窗口
from typing import List
from collections import defaultdict
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)
        ans = 0
        for vec in pos.values():
            j = 0
            for i in range(len(vec)):
                print(vec[i],vec[j],i-j)
                # 缩小窗口，直到不同元素数量小于等于 k
                # (i - j) 表示窗口内不同元素的数量
                # vec[i] - vec[j] 表示窗口内元素的数量
                while vec[i] - vec[j] - (i - j) > k:
                    j += 1
                ans = max(ans, i - j + 1)

        return ans


""" 这种方法对于一些测试用例并不适用
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        t = [0, ] * (len(nums) + 1)
        dist = {}
        t1 = [0, ] * (len(nums) + 1)
        const = 0
        tc = 1
        if len(nums) == 1:
            return 1
        for i in range(len(nums)):
            if i >= 1:
                if nums[i] == nums[i - 1]:
                    tc += 1
                else:
                    tc = 1
                if tc > const:
                    const = tc

            t[nums[i]] += 1
            if nums[i] not in dist.keys():
                dist[nums[i]] = 0
            else:
                dist[nums[i]] += i - t1[nums[i]] - 1
            t1[nums[i]] = i
        print(dist)
        mx = 0
        for i in range(1, len(t)):
            if k == 0:
                return const
            if t[i] > mx and dist[i] <= k:
                mx = t[i]
        return mx
"""