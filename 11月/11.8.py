# 差分学习Link:https://leetcode.cn/problems/car-pooling/solutions/2550264/suan-fa-xiao-ke-tang-chai-fen-shu-zu-fu-9d4ra/
# source:https://leetcode.cn/problems/divide-intervals-into-minimum-number-of-groups/ 差分+贪心
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        right = 0
        for _, j in intervals:
            right = max(right, j)
        total = [0 for _ in range(right+2)]

        for i, j in intervals:
            total[i] += 1
            total[j+1] -= 1
        ans = 0
        for i in range(1, len(total)):
            total[i] += total[i-1]
            ans = max(ans, total[i])
        return ans

# source:https://leetcode.cn/submissions/detail/579046788/ 差分
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0 for _ in range(n+2)]
        for i, j, value in bookings:
            ans[i] += value
            ans[j+1] -= value
            # print(ans)
        for i in range(1, len(ans)):
            ans[i] += ans[i-1]
        return ans[1:-1]

# source:https://leetcode.cn/submissions/detail/579040335/ 差分
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        store = [0 for _ in range(1001)]
        for num, i, j in trips:
            store[i] += num
            store[j] -= num
        for i in range(len(store)-1):
            store[i+1] += store[i]
        for v in store:
            if v > capacity:
                return False
        return True

# source:https://leetcode.cn/problems/shifting-letters-ii/ 差分
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        total = [0 for _ in range(len(s)+2)]
        for i, j, d in shifts:
            if d:
                total[i+1] += 1
                total[j+2] -= 1
            else:
                total[i+1] += -1
                total[j+2] -= -1
        # print(total)
        for i in range(1, len(total)-1):
            total[i+1] += total[i]
        # print(total[1:-1])
        res = ''
        for i, v in enumerate(total[1:-1]):
            num = ord(s[i]) + v
            if num < 97:
                res += chr(122 - (96 - num)%26)
            elif num > 122:
                res += chr((num - 123)%26 + 97)
            else:
                res += chr(num)
        return res