# source:https://leetcode.cn/problems/find-smallest-letter-greater-than-target/  二分
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = 0
        j = len(letters ) -1
        while i<= j:
            mid = (i + j) // 2
            if letters[mid] == target:
                while mid < len(letters) - 1:
                    mid += 1
                    if letters[mid] > target:
                        return letters[mid]
                else:
                    return letters[0]
            elif letters[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        t = max(i, j)
        if t == len(letters):
            return letters[0]
        else:
            return letters[t]

# source:https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer/description/ 二分


class Solution1:
    def maximumCount(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == 0:
                left = right = inf
                t1 = mid + 1
                t2 = mid - 1
                while 1:
                    if t1 == len(nums) or nums[t1] > 0:
                        right = t1
                    else:
                        t1 += 1
                    if t2 == -1 or nums[t2] < 0:
                        left = t2
                    else:
                        t2 -= 1
                    if left != inf and right != inf:
                        return max(left + 1, len(nums) - right)
            elif nums[mid] > 0:
                j = mid - 1
            else:
                i = mid + 1
        return max(i, len(nums) - i)


