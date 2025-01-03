# source:https://leetcode.cn/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/ 滑窗
from cmath import inf
from typing import List


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = inf
        i = count = 0
        for j, v in enumerate(blocks):
            if v == 'W':
                count += 1
            if j+1 > k:
                if blocks[i] == 'W':
                    count -= 1
                i += 1
            if j+1 >= k:
                res = min(res, count)
                
        return res

# source: https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/description/ 逆向思维+滑窗
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        i = j = 0
        res = inf
        t = 0
        total = sum(nums)
        while j < len(nums):
            t += nums[j]
            while total - t < x and i <= j:
                t -= nums[i]
                i += 1
            if total - t == x:
                res = min(res, i+len(nums)-j-1)
            j += 1
        return -1 if res == inf else res
        # def dfs(v, left, right, count): dfs超时
        #     print(v)
        #     nonlocal res
        #     if left > right or v < 0:
        #         return
        #     if v == 0:
        #         res = min(res, count)
        #         return 
        #     dfs(v - nums[left], left+1, right, count+1)
        #     dfs(v - nums[right], left, right-1, count+1)

        # res = inf
        # dfs(x, 0, len(nums)-1, 0)
        # return -1 if res == inf else res