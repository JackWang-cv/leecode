# source:https://leetcode.cn/problems/minimize-maximum-of-array/submissions/589821435/ 二分
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def find(value):
            temp = nums[-1]
            for i in range(len(nums)-1, 0, -1):    
                temp = nums[i-1]+ (temp-value if temp > value else 0)
            return temp > value

        i, j = 0, max(nums)
        while i < j:
            mid = (i+j)//2
            if find(mid):
                i = mid+1
            else:
                j = mid
        return i

# source:https://leetcode.cn/problems/maximize-score-of-numbers-in-ranges/ 二分+贪心
class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()

        def check(score: int) -> bool:
            x = -inf
            for s in start:
                x = max(x + score, s)  # x 必须 >= 区间左端点 s
                if x > s + d:
                    return False
            return True

        left, right = 0, (start[-1] + d )
        while left < right:
            mid = (left + right+1) // 2
            if check(mid):
                left = mid
            else:
                right = mid-1
        return left