# source:https://leetcode.cn/problems/find-peak-element/description/  二分
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if mid == 0:
                if len(nums) == 1 or (nums[mid] > nums[mid + 1]):
                    return mid
                else:
                    i += 1
            elif mid == len(nums) - 1 and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            else:
                if nums[mid - 1] > nums[mid]:
                    j = mid - 1
                elif nums[mid] < nums[mid + 1]:
                    i = mid + 1

# source:https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/description/  二分


class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for index1 in range(len(numbers) - 1):
            i = index1 + 1
            j = len(numbers) - 1
            temp = target - numbers[index1]
            if numbers[j] < temp:
                continue
            while i <= j:
                mid = (i + j) // 2
                if numbers[mid] == temp:
                    return [index1 + 1, mid + 1]
                elif numbers[mid] > temp:
                    j = mid - 1
                else:
                    i = mid + 1


if __name__ == "__main__":
    S = Solution()
    print(S.findPeakElement([1,2,3,4,3]))
    S1 = Solution1()
    print(S1.twoSum([1,2,3,4], 5))