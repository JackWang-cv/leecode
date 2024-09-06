# source:https://leetcode.cn/problems/jump-game-ii/description/ 贪心
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step

x = Solution()
x.jump([10, 9, 8, 7, 6, 5, 4 ,3, 2, 1, 0])

