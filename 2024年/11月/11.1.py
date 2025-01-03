# source:https://leetcode.cn/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/description/
from typing import List

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prefix_sum = 0
        seen = {0}  # 存储能形成目标和的前缀和
        count = 0   # 记录满足条件的子数组数量
        
        for num in nums:
            prefix_sum += num
            
            # 检查是否可以形成一个和为 target 的子数组
            if prefix_sum - target in seen:
                count += 1  # 记录一个符合条件的子数组
                seen = {0}  # 重置 seen 保证子数组不重叠
                prefix_sum = 0  # 重置 prefix_sum
            
            # 记录当前前缀和
            seen.add(prefix_sum)
        
        return count

# source:https://leetcode.cn/problems/sum-of-absolute-differences-in-a-sorted-array/description/ 前缀和+推导
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = [0 for _ in range(len(nums)+1)]
        for i, v in enumerate(nums):
            total[i+1] = total[i] + v
        ans = []
        for i in range(len(nums)):
            res = i * nums[i] - total[i] + (total[-1] - total[i+1]) - (len(nums)-i-1)*nums[i]
            ans.append(res)
        return ans

# source:https://leetcode.cn/problems/find-longest-subarray-lcci/
class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        d = defaultdict(int)
        store = defaultdict(list)
        store[0] = [-1, '']
        res = 0
        res_index = []
        for i, v in enumerate(array):
            if 'a' <= v <= 'z' or 'A' <= v <= 'Z':
                d[0] += 1
            else:
                d[1] += 1
            if store[d[1] - d[0]]:
                if res < i - store[d[1] - d[0]][0]+1:
                    res = i - store[d[1] - d[0]][0]+1
                    res_index = [store[d[1] - d[0]][0]+1, i+1]
                elif res == i - store[d[1] - d[0]][0]+1:
                    if array[res_index[0]] > store[d[1] - d[0]][1]:
                        res_index = [store[d[1] - d[0]][0]+1, i+1]
            else:
                store[d[1] - d[0]] = [i, v]
            # print(i, res_index)
        return array[res_index[0]:res_index[1]] if res_index else res_index