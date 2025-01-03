# source:https://leetcode.cn/problems/maximum-number-of-robots-within-budget/ 堆+滑窗
from typing import List
from sortedcontainers import SortedList


class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        ans = 0
        i = 0
        s = SortedList()
        total = 0
        for j, v in enumerate(chargeTimes):
            s.add(v)
            total += runningCosts[j]
            while s and i<=j and s[-1] + len(s)*total > budget:
                s.remove(chargeTimes[i])
                total -= runningCosts[i]
                i += 1
            ans = max(ans, len(s))
        return ans

# source:https://leetcode.cn/problems/word-search/description/ dfs
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        def dfs(t, index):
            if index == len(word):
                return True
            for m, n in [[1,0],[0,-1],[-1,0],[0,1]]:
                x = t[0]+m
                y = t[1]+n
                if 0 <= x < len(board) and 0 <= y < len(board[0]):
                    if not visit[x][y] and board[x][y] == word[index]:
                        visit[x][y] = 1
                        if dfs([x, y], index+1):
                            return True
                        visit[x][y] = 0
            return 0
        for i in range(len(visit)):
            for j in range(len(visit[0])):
                if not visit[i][j] and board[i][j] == word[0]:
                    visit[i][j] = 1
                    if dfs([i, j],1):
                        return True
                    visit[i][j] = 0
        return False

# source:https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/description/
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)

        l = 2

        for r in range(2, len(nums)):
            if nums[l - 2] != nums[r]:
                nums[l] = nums[r]
                l += 1

        return l