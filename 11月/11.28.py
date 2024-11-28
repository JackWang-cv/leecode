# source:https://leetcode.cn/problems/k-concatenation-maximum-sum/ DP 最大子数组和
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mx = max(arr[0], 0)
        f0 = arr[0]
        n = len(arr)
        if k == 1:
            for i in range(1, n):
                f0 = max(f0+arr[i], arr[i])
                mx = max(mx, f0)
            return mx
        else:
            for i in range(1, 2*n):
                if f0 + arr[i%n] > arr[i%n]:
                    f0 += arr[i%n]
                    if mx < f0:
                        mx = f0
                else:
                    f0 = arr[i%n]
                    if mx < f0:
                        mx = f0
        # print(mx)
        return max(mx, mx + sum(arr)*(k-2))%(10**9+7)

# source:https://leetcode.cn/problems/maximum-total-reward-using-operations-i/
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        nums = sorted(set(rewardValues))
        m = nums[-1] << 1
        f = [False] * m
        f[0] = True
        for v in nums:
            for j in range(m):
                if 0 <= j - v < v:
                    f[j] |= f[j - v]
        ans = m - 1
        while not f[ans]:
            ans -= 1
        return ans

#source:https://leetcode.cn/problems/sliding-window-median/
from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        s = SortedList()
        i = 0
        ans = []
        for j, v in enumerate(nums):
            s.add(v)
            if j-i+1 > k:
                s.remove(nums[i])
                i += 1
            if j-i+1 == k:
                if k&1:
                    ans.append(s[k//2])
                else:
                    ans.append((s[k//2 - 1]+s[k//2])/2)
        return ans

# source:https://leetcode.cn/problems/sliding-window-median/
from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        s = SortedList()
        i = 0
        ans = []
        for j, v in enumerate(nums):
            s.add(v)
            if j-i+1 > k:
                s.remove(nums[i])
                i += 1
            if j-i+1 == k:
                if k&1:
                    ans.append(s[k//2])
                else:
                    ans.append((s[k//2 - 1]+s[k//2])/2)
        return ans

# source:蓝桥杯热身题 前缀和异或
import os
import sys

# 请在此输入您的代码
N = int(input())
L = [int(i) for i in input().split()]
store = [0]
for i, v in enumerate(L):
  store.append(store[-1]^v)

final = store[-1]
for i in range(1, len(store)-1):
  if final ^ store[i] == store[i]:
    print('YES')
    break
else:
  print('NO')