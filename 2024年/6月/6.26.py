# source:https://leetcode.cn/problems/search-in-rotated-sorted-array/ 二分
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        new_n = sorted(nums)
        i = 0
        j = len(nums) - 1
        while i <= j:
            print(i, j)
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[i] > nums[mid]:
                    j = mid - 1
                else:
                    if target >= nums[i]:
                        j = mid - 1
                    else:
                        i = mid + 1
            else:
                if nums[j] > nums[mid] and target <= nums[j]:
                    i = mid + 1
                elif nums[j] > nums[mid] and target > nums[j]:
                    j = mid - 1
                else:
                    i = mid + 1

        return -1


s = Solution()
print(s.search([5,1,2,3,4],1))