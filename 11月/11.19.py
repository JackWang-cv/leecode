# source:https://leetcode.cn/problems/minimum-remove-to-make-valid-parentheses/ 栈
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, v in enumerate(s):
            if v == '(':
                stack.append([v, i])
            elif v == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append([v, i])
        ans = ''
        i = 0
        for j, v in enumerate(s):
            if i < len(stack) and j == stack[i][1]:
                i += 1
                continue
            else:
                ans += v
        return ans

# source:https://leetcode.cn/problems/reveal-cards-in-increasing-order/ 队列
from collections import deque
import heapq
from typing import List
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        d = deque()
        L = sorted(deck)
        # print(L)
        for i in range(len(L)-1, -1, -1):
            if not d:
                d.append(L[i])
            else:
                t = d.pop()
                d.appendleft(t)
                d.appendleft(L[i])
        ans = []
        while d:
            ans.append(d.popleft())
        return ans

# source:https://leetcode.cn/problems/sliding-window-maximum/submissions/581669226/ 优先队列 == 堆 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        
        return ans
