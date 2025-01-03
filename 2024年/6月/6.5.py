# source:https://leetcode.cn/problems/distribute-elements-into-two-arrays-i/
from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        res1 = [nums[0]]
        res2 = [nums[1]]
        i = 2
        while i < len(nums):
            if res1[-1] > res2[-1] :
                res1.append(nums[i])
            else:
                res2.append(nums[i])
            i += 1
        return res1 + res2

# source:https://leetcode.cn/problems/distribute-elements-into-two-arrays-ii/ 暴力解
class Solution1:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        sorted_arr1 = [nums[0]]
        sorted_arr2 = [nums[1]]

        for i in range(2, len(nums)):
            index1 = bisect_left(sorted_arr1, nums[i] + 1)
            index2 = bisect_left(sorted_arr2, nums[i] + 1)
            count1 = len(arr1) - index1
            count2 = len(arr2) - index2
            if count1 > count2:
                arr1.append(nums[i])
                sorted_arr1.insert(index1, nums[i])
            elif count1 < count2:
                arr2.append(nums[i])
                sorted_arr2.insert(index2, nums[i])
            else:
                if len(arr1) < len(arr2):
                    arr1.append(nums[i])
                    sorted_arr1.insert(index1, nums[i])
                elif len(arr1) > len(arr2):
                    arr2.append(nums[i])
                    sorted_arr2.insert(index2, nums[i])
                else:
                    arr1.append(nums[i])
                    sorted_arr1.insert(index1, nums[i])
        return arr1 + arr2
