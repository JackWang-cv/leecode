# source:https://leetcode.cn/problems/detonate-the-maximum-bombs/description/ bfs
from typing import List
import math

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dfs(i):
            stack = [i]
            visited = set()
            visited.add(i)
            count = 0

            while stack:
                bomb = stack.pop()
                count += 1
                x, y, r = bombs[bomb]
                for j in range(len(bombs)):
                    if j not in visited:
                        vx, vy, vr = bombs[j]
                        if math.sqrt((x - vx) ** 2 + (y - vy) ** 2) <= r:
                            stack.append(j)
                            visited.add(j)
            return count

        max_detonations = 0

        for i in range(len(bombs)):
            max_detonations = max(max_detonations, dfs(i))

        return max_detonations

# source:https://leetcode.cn/problems/k-diff-pairs-in-an-array/ 二分
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        last_val = -math.inf
        right = nums[1:]
        res = 0
        for index in range(len(nums) - 1):
            if nums[index] == last_val:
                right.remove(right[0])
                continue
            last_val = nums[index]
            i = 0
            j = len(right) - 1
            while i <= j:
                mid = (i + j) // 2
                if abs(nums[index] - right[mid]) == k:
                    res += 1
                    break
                elif abs(nums[index] - right[mid]) > k:
                    j = mid - 1
                else:
                    i = mid + 1
            right.remove(right[0])
        return res





