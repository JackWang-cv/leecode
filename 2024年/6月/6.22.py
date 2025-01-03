# source: https://leetcode.cn/problems/3sum/description/ 和6.17有异曲同工之妙
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # 跳过重复的数
                continue
            j = i + 1
            k = len(nums) - 1

            while j < k:
                t = nums[i] + nums[j] + nums[k]
                if t == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k - 1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1
                elif t < 0:
                    j += 1
                elif t > 0:
                    k -= 1
        return res
