# source:https://leetcode.cn/problems/find-missing-observations/
from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        All = mean * (len(rolls) + n)
        dist = All - sum(rolls)
        res = []
        t = 0
        ave = dist // n

        if (ave >= 6 and dist % 6 != 0) or ave == 0 or dist <= 0:
            return res

        while 1:
            if dist - ave * (n - 1) > 6:
                if ave == 6:
                    return []
                res.append(ave + 1)
                t = (ave + 1)
            elif dist - ave * (n - 1) < 0:
                if (ave - 1) == 0:
                    return []
                res.append(ave - 1)
                t = (ave - 1)
            else:
                res.append(ave)
                t = ave
            dist -= t
            n -= 1
            if n == 1:
                res.append(dist)
                break
            elif n == 0:
                break
        return res


