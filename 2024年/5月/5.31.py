# source:https://leetcode.cn/problems/find-missing-and-repeated-values/
from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hashdict = {}
        double = 0
        absent = 0
        sign = [0, ] * (pow(len(grid), 2) + 1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                hashdict[grid[i][j]] = hashdict.get(grid[i][j], 0) + 1
                if hashdict[grid[i][j]] == 2:
                    double = grid[i][j]
                sign[grid[i][j]] += 1
        for i in range(1, len(sign)):
            if sign[i] == 0:
                absent = i
                break
        return [double, absent]


