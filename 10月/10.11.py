# source:https://leetcode.cn/problems/4sum/ 三指针 二分
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)-3):
            if nums[i] == nums[i-1] and i > 0:
                continue
            for j in range(i+1, len(nums)-2):
                if nums[j] == nums[j-1] and j > i+1:
                    continue
                for k in range(j+1, len(nums)-1):
                    if nums[k] == nums[k-1] and k > j+1:
                        continue
                    reminder = target - (nums[i]+nums[j]+nums[k])
                    left = k + 1
                    right = len(nums)-1
                    while left <= right:
                        mid = (left+right)//2
                        if nums[mid] == reminder:
                            ans.append([nums[i], nums[j], nums[k], reminder])
                            break
                        elif nums[mid] > reminder:
                            right = mid - 1
                        else:
                            left = mid + 1
        return ans

# source:https://leetcode.cn/problems/permutation-sequence/description/
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        count = 0
        visit = [0 for _ in range(n+1)]
        def dfs(s):
            nonlocal count
            if len(s) == n:
                count += 1
                if count == k:
                    return s
                return ''
             
            for i in range(1, n+1):
                if not visit[i]:
                    visit[i] = 1
                    res = dfs(s + str(i))
                    visit[i] = 0
                    if res:
                        return res              
        return dfs('')

# source:https://leetcode.cn/problems/total-hamming-distance/description/
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        mx = max(nums)
        i = count = 0
        while mx >> i:
            c_o = c_z = 0
            for v in nums:
                if (v >> i) & 1:
                    c_o += 1
                else:
                    c_z += 1
            count += c_o * c_z
            i += 1
        return count