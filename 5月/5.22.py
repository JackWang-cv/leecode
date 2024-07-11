# source : https://leetcode.cn/problems/find-players-with-zero-or-one-losses/ 经典空间换时间
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        judge = [0, ] * (pow(10, 5) + 1)
        exist = [0, ] * (pow(10, 5) + 1)
        win = []
        defeat = []
        t = 0
        for m in matches:
            if t < max(m):
                t = max(m)
            exist[m[0]] = 1
            exist[m[1]] = 1
            if judge[m[1]] == 0:
                judge[m[1]] = 1
            else:
                judge[m[1]] += 1

        for i in range(1, t + 1, 1):
            if judge[i] == 0 and exist[i] == 1:
                win.append(i)
            elif judge[i] == 1:
                defeat.append(i)
        return [win, defeat]