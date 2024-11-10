# source:https://leetcode.cn/submissions/detail/579457794/ 前缀和 队列 贪心 差分
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        diff = [0] * (n + 1)
        ans, revCnt = 0, 0
        for i in range(n):
            revCnt += diff[i]
            if (A[i] + revCnt) % 2 == 0: #需要翻转
                if i + K > n: #出界了，就结束
                    return -1
                ans += 1 # 翻转次数
                revCnt += 1 # 左侧位置+1 直接传递到 revCnt 上
                diff[i + K] -= 1 # 右端点+1 位置 -1
        return ans
# 法二：
from collections import deque
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        total = [0 for _ in range(len(nums))]
        ans = inc = 0
        stack = deque()
        for i in range(len(nums)-k+1):
            if stack and i == stack[0]:
                stack.popleft()
                inc -= 1
            total[i] += inc
            if nums[i] == 0:
                if total[i] % 2 == 0:
                    ans += 1
                    stack.append(i+k)
                    inc += 1
            else:
                if total[i] % 2 != 0:
                    ans += 1
                    stack.append(i+k)
                    inc += 1     
        # print(total, stack)           
        for i in range(len(nums)-k+1, len(nums)):
            if stack and i == stack[0]:
                stack.popleft()
                inc -= 1
            # print(i, inc)
            total[i] += inc
            if nums[i] == 1 and total[i]%2 != 0:
                return -1
            elif nums[i] == 0 and total[i]%2 == 0:
                return -1
        return ans