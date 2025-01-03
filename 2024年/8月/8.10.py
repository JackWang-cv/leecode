# source:https://leetcode.cn/problems/k-radius-subarray-averages/description/ 滑窗
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = []
        j = t = 0
        flag = 1
        for i in range(len(nums)):
            if i-k >= 0 and i+k+1 <= len(nums):
                if flag:
                    j = i - k
                    t = sum(nums[i-k:i+k+1])
                    flag = 0
                else:
                    t -= nums[j]
                    t += nums[i+k]
                    j += 1
                res.append(t//(2*k+1))
            else:
                res.append(-1)
        return res

# source:https://leetcode.cn/problems/longest-nice-subarray/  滑窗
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        i = j = 0
        res = 0
        t = 0
        while j < len(nums):
            while nums[j] & t and i <= j:
                t -= nums[i]
                i += 1
            t = nums[j] | t
            res = max(res, j - i + 1)
            j += 1
        return res