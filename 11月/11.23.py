# source:https://leetcode.cn/problems/find-the-number-of-winning-players/ hashtable 
from collections import defaultdict
from typing import List


# class Solution:
#     def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
#         ans = 0
#         d = defaultdict(list)
#         for i, j in pick:
#             d[i].append(j)

#         dic = defaultdict(int)
#         for v in d.keys():
#             temp = d[v]
#             mx = 0
#             dic.clear()
#             for value in d[v]:
#                 dic[value] += 1
#                 if dic[value] > mx:
#                     mx = dic[value]
#                 if mx > v:
#                     ans += 1
#                     break
#         return ans

# source: 手写堆排序
nums = [22, 1, 23, 34, 4, 51, 14, 16, 24]

def heapify(array, node):
    smallest = node
    left = node*2 + 1
    right = node*2 + 2
    if left < len(nums) and array[smallest] > array[left]:
        smallest = left        
    if right < len(nums) and array[smallest] > array[right]:
        smallest = right
    if smallest != node:
        array[smallest], array[node] = array[node], array[smallest]
        heapify(array, smallest)

for i in range(len(nums)//2 - 1, -1, -1):
    heapify(nums, i)
# print(nums)
ans = []
while nums:
    nums[0], nums[-1] = nums[-1], nums[0]
    ans.append(nums.pop())
    heapify(nums, 0)
print(ans)

# source:手写归并排序
def merge(array1, array2):
    i, j = 0, 0
    res = []
    len1, len2 = len(array1), len(array2)
    for _ in range(len1+len2):
        if i == len1:
            res += array2[j:]
            break
        elif j == len2:
            res += array1[i:]
            break
        if array1[i] < array2[j]:
            res.append(array1[i])
            i += 1
        else:
            res.append(array2[j])
            j += 1
    return res

def merge_sort(array):
    # 如果数组长度小于等于 1，直接返回
    if len(array) <= 1:
        return array
    
    # 分割数组
    mid = len(array) // 2
    left = merge_sort(array[:mid])  # 递归排序左半部分
    right = merge_sort(array[mid:])  # 递归排序右半部分

    # 合并已排序的两部分
    return merge(left, right)

ans = merge_sort(nums)
print(ans)

# source: 手写快速排序
def quick_sort(array):
    # 如果数组长度小于等于 1，直接返回
    if len(array) <= 1:
        return array
    
    # 选择一个基准值（这里选择数组的最后一个元素）
    pivot = array[-1]
    
    # 分为三部分：小于基准值、等于基准值、大于基准值
    left = [x for x in array[:-1] if x < pivot]  # 小于基准值
    equal = [x for x in array if x == pivot]  # 等于基准值
    right = [x for x in array[:-1] if x > pivot]  # 大于基准值
    
    # 对左右两部分递归排序，并合并结果
    return quick_sort(left) + equal + quick_sort(right)

sorted_nums = quick_sort(nums)
print(sorted_nums)

# source:https://leetcode.cn/problems/maximum-subarray/description/ 最大子数组和 dp 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 回溯 记忆化搜索
        # @cache
        # def dfs(i):
        #     if i < 0:
        #         return 0
        #     return max(dfs(i-1) + nums[i], nums[i])
        # return max(dfs(i) for i in range(len(nums)))

        # dp
        # f = [0 for _ in range(len(nums)+1)]
        # f[0] = 0
        # mx = -inf
        # for i in range(len(nums)):
        #     f[i+1] = max(f[i] + nums[i], nums[i])
        #     mx = max(f[i+1], mx)
        # # print(f)
        # return mx

        # 优化空间dp
        # f0 = 0
        # mx = -inf
        # for i in range(len(nums)):
        #     f0 = max(f0 + nums[i], nums[i])
        #     mx = max(f0, mx)
        # return mx
        pass

# source:https://leetcode.cn/problems/maximum-product-subarray/submissions/582633538/ 上一题变形dp 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        f0, f1 = nums[0], nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            mx, mn = f0, f1
            f0 = max(f0*nums[i], max(nums[i], mn*nums[i]))           
            f1 = min(f1*nums[i], min(nums[i], mx*nums[i]))
            ans = max(f0, ans)
        return ans