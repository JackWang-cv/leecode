# source:https://leetcode.cn/problems/minimum-absolute-sum-difference/ 二分
from typing import List


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        count = 0
        mx = 0
        nums = sorted(nums1)

        for v in range(len(nums1)):
            sub = abs(nums1[v] - nums2[v])
            count += sub
            i = 0
            j = len(nums1) - 1
            while i < j:
                # 循环不变量 i True j False
                mid = (i + j) // 2
                if nums2[v] >= nums[mid]:
                    i = mid + 1
                else:
                    j = mid
            if i == len(nums1):
                new_sub = abs(nums2[v] - nums[i - 1])
            elif i == 0:
                new_sub = abs(nums2[v] - nums[i])
            else:
                new_sub = min(abs(nums2[v] - nums[i]), abs(nums2[v] - nums[i - 1]))
            mx = max(sub - new_sub, mx)
        count -= mx
        return count % (10 ** 9 + 7)

# source:https://leetcode.cn/problems/find-the-smallest-divisor-given-a-threshold/
class Solution1:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        i = 1
        j = max(nums)
        while i<j:
            count = 0
            mid = (i+j)//2
            for v in nums:
                t = (v // mid)
                count += t if t*mid == v else t + 1
            if count > threshold:
                i = mid+1
            else:
                j = mid
        return i

X = Solution1()
print(X.smallestDivisor([1,2,3,4], 2))