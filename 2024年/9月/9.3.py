# source:https://leetcode.cn/problems/maximum-strength-of-a-group/ 排序+贪心
from typing import List, Optional


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort(reverse=True)
        q = ans = 1
        index = len(nums)
        flag = 1
        for i, v in enumerate(nums):
            if v > 0:
                ans *= v
            elif v == 0:
                if i == 0 and nums[-1] == 0:
                    return 0
                continue
            else:
                if flag:
                    flag = 0
                    index = i
                q *= v
        t = (len(nums)-index)
        if t % 2 !=0:
            q //= nums[index]
            if nums[0] == 0 and t == 1:
                return 0
        ans *= q
        return ans

# source:https://leetcode.cn/problems/next-greater-node-in-linked-list/description/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        q = head
        res = []
        while q:
            while stack and stack[-1].val < q.val:
                t = stack.pop()
                t.val = q.val
            stack.append(q)
            q = q.next
        while stack:
            t = stack.pop()
            t.val = 0
        q = head
        while q:
            res.append(q.val)            
            q = q.next
        return res

# source:https://leetcode.cn/problems/maximum-width-ramp/description/
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans = 0
        stack = []
        n = len(nums)
        for i, num in enumerate(nums):
            while not stack or num < nums[stack[-1]]:
                stack.append(i)
        
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                ans = max(ans, i - stack.pop())
        return ans

# source:https://leetcode.cn/problems/car-fleet/  有难度 拿时间压栈
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [0 for _ in range(target)]
        for i in range(len(position)):
            time[position[i]] = (target - position[i]) / speed[i] + 1 
        stack = []
        for i in range(target-1, -1, -1):
            if time[i] > 0:
                if not stack:
                    stack.append(time[i])
                elif time[i] > stack[-1]:
                    stack.append(time[i])
                else:
                    pass
        return len(stack)
