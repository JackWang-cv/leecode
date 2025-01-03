# # source:https://leetcode.cn/problems/alternating-groups-ii/description/ 滑窗
# from collections import defaultdict
# import heapq
# from typing import List


# class Solution:
#     def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
#         # 判断相邻两个是否相等
#         sign = []
#         n = len(colors)
#         for i in range(2*n-1):
#             if colors[i%n] == colors[(i+1)%n]:
#                 sign.append(0)
#             else:
#                 sign.append(1)
#         # print(sign)
#         i, cnt = 0, 0
#         ans = 0
#         for j, v in enumerate(sign):
#             if i == n-1:
#                 break
#             cnt += v
#             if j-i+1 > k-1:
#                 cnt -= sign[i]
#                 i += 1
#             if j-i+1 == k-1:
#                 # print(cnt)
#                 if cnt == k-1:
#                     ans += 1
#         return ans

# # source:https://leetcode.cn/problems/ugly-number-ii/ 堆
# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         d = defaultdict(int)
#         factors = [2, 3, 5]
#         nums = [1]
#         d[1] = 1
#         heapq.heapify(nums)
#         for i in range(n-1):
#             x = heapq.heappop(nums)
#             for factor in factors:
#                 if d[x*factor] == 0:
#                     d[x*factor] = 1
#                     heapq.heappush(nums, x*factor)
#         return heapq.heappop(nums)

# # source:https://leetcode.cn/problems/maximum-absolute-sum-of-any-subarray/ 最大子数组和
# class Solution:
#     def maxAbsoluteSum(self, nums: List[int]) -> int:
#         ans = abs(nums[0])
#         f0, f1 = nums[0], nums[0]
#         mx, mn = ans, ans
#         for i in range(1, len(nums)):
#             v = nums[i]
#             f0 = max(f0+v, v)
#             f1 = min(f1+v, v)
#             ans = max(ans, abs(f0), abs(f1))
#         return ans


# 蓝桥杯测试题
import os
import sys

# 请在此输入您的代码
N = eval(input(' '))
L = [int(i) for i in input(' ').split()]
stack = []
# print(N, L)
def init():
    stack.clear()
    return [-1 for _ in range(len(L))]

def p(array):
    for v in array:
        print(v, end = ' ')
    print('\n')
ans = init()
for i, v in enumerate(L):
  if i == 0:
    ans[i] = -1
    stack.append(v)
  else:
    while stack and stack[-1] <= v:
      stack.pop()
    if stack:
      ans[i] = stack[-1]
    else:
      ans[i] = -1
    stack.append(v)
p(ans)

ans = init()
for i in range(len(L)-1, -1, -1):
  if i == len(L)-1:
    stack.append(L[i])
  else:
    while stack and stack[-1] <= L[i]:
      stack.pop()
    if stack:
      ans[i] = stack[-1]
    else:
      ans[i] = -1
    stack.append(L[i])
p(ans)

ans = init()
for i, v in enumerate(L):
  if i == 0:
    ans[i] = -1
    stack.append(v)
  else:
    while stack and stack[-1] >= v:
      stack.pop()
    if stack:
      ans[i] = stack[-1]
    else:
      ans[i] = -1
    stack.append(v)
p(ans)

ans = init()
for i in range(len(L)-1, -1, -1):
  if i == len(L)-1:
    stack.append(L[i])
  else:
    while stack and stack[-1] >= L[i]:
      stack.pop()
    if stack:
      ans[i] = stack[-1]
    else:
      ans[i] = -1
    stack.append(L[i])
p(ans)

