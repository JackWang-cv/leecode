# source:https://leetcode.cn/problems/6CE719/description/?envType=daily-question&envId=2024-06-21
from typing import List


class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        mx = count = 0
        for i in range(1, len(temperatureA)):
            t1 = temperatureA[i] - temperatureA[i-1]
            t2 = temperatureB[i] - temperatureB[i-1]

            if (t1 < 0 and t2 < 0) or (t1 == 0 and t2 == 0) or (t1 > 0 and t2 > 0):
                count += 1
                mx = max(mx, count)
            else:
                count = 0
        return mx
