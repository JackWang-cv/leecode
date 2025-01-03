# source:https://leetcode.cn/problems/clear-digits/description/ 栈
from cmath import inf
from typing import List


class Solution:
    def clearDigits(self, s: str) -> str:
        new_s = []
        for v in s:
            if new_s and new_s[-1] >= 'a' and '0' <= v <= '9':
                new_s.pop()
                continue
            new_s.append(v)
        return ''.join(new_s)

# source:https://leetcode.cn/problems/next-permutation/description/
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if sorted(nums, reverse=True) == nums:
            nums.sort()
        else:
            temp = -1
            mn = inf
            index = len(nums)
            for i in range(len(nums)-1, -1,-1):
                if nums[i] > nums[i-1]:
                    temp = nums[i-1]
                    for j in range(i, len(nums), 1):
                        if nums[j] > temp:
                            if mn > nums[j]:
                                mn = nums[j]
                                index = j
                    # 计算比目标大的最小值
                    nums[i-1] = nums[index]
                    nums[index] = temp
                    for m in range(i, len(nums)-1, 1):
                        temp = nums[m]
                        mn = inf
                        for n in range(m+1, len(nums), 1):
                            if nums[n] < temp:
                                if mn > nums[n]:
                                    mn = nums[n]
                                    index = n
                        if mn != inf:
                            nums[m] = nums[index]
                            nums[index] = temp
                    break

# source:https://leetcode.cn/problems/largest-rectangle-in-histogram/ 单调栈
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n
        st = []
        for i, x in enumerate(heights):
            while st and x <= heights[st[-1]]:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)

        right = [n] * n
        st.clear()
        for i in range(n - 1, -1, -1):
            x = heights[i]
            while st and x <= heights[st[-1]]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)

        ans = 0
        for h, l, r in zip(heights, left, right):
            ans = max(ans, h * (r - l - 1))
        return ans

