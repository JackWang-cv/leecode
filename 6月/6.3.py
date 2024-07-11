# source:https://leetcode.cn/problems/distribute-candies-to-people/
from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        i = 0
        Ind = 1
        ans = [0,]*num_people
        while candies >0:
            if i==num_people:
                i = 0
            if Ind > candies:
                ans[i] += candies
                break
            ans[i] += Ind
            candies -= Ind
            Ind += 1
            i += 1
        return ans


# 法二：数学
class Solution1:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = num_people
        # how many people received complete gifts
        p = int((2 * candies + 0.25) ** 0.5 - 0.5)
        remaining = int(candies - (p + 1) * p * 0.5)
        rows, cols = p // n, p % n

        d = [0] * n
        for i in range(n):
            # complete rows
            d[i] = (i + 1) * rows + int(rows * (rows - 1) * 0.5) * n
            # cols in the last row
            if i < cols:
                d[i] += i + 1 + rows * n
        # remaining candies
        d[cols] += remaining
        return d

