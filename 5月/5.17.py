# source:https://leetcode.cn/problems/most-profit-assigning-work/

from typing import List


class Solution:
    def find(self, left, right, w, L, max_profit):
        while left <= right:
            mid = (left + right) // 2
            if L[mid] <= w:
                left = mid + 1
            else:
                right = mid - 1
        return right

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        max_profit = {}
        for i in range(len(difficulty)):
            if difficulty[i] not in max_profit:
                max_profit[difficulty[i]] = profit[i]
            else:
                max_profit[difficulty[i]] = max(profit[i], max_profit[difficulty[i]])

        L = sorted(max_profit.keys())
        max_profit_so_far = 0
        for i in range(len(L)):
            max_profit_so_far = max(max_profit_so_far, max_profit[L[i]])
            max_profit[L[i]] = max_profit_so_far

        total_profit = 0
        for w in worker:
            if w < L[0]:
                continue
            idx = self.find(0, len(L) - 1, w, L, max_profit)
            total_profit += max_profit[L[idx]]

        return total_profit
# 示例测试
solution = Solution()
difficulty = [68, 35, 52, 47, 86]
profit = [67, 17, 1, 81, 3]
worker = [92, 10, 85, 84, 82]
print(solution.maxProfitAssignment(difficulty, profit, worker))  # 应该输出211