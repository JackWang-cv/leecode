# source:https://leetcode.cn/submissions/detail/579240893/ 枚举
from collections import defaultdict
from typing import List


class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.d = defaultdict(list)
        self.padding = [[0 for _ in range(len(grid[0])+2)] for _ in range(len(grid)+2)]
        row, col = len(self.padding), len(self.padding[0])
        for i in range(1, row-1):
            for j in range(1, col-1):
                self.padding[i][j] = grid[i-1][j-1]
        for i in range(1, row-1):
            for j in range(1, col-1):
                neighbor = self.padding[i-1][j] + self.padding[i][j-1] + self.padding[i][j+1] + self.padding[i+1][j]
                systemmic = self.padding[i-1][j-1] + self.padding[i+1][j+1] + self.padding[i-1][j+1] + self.padding[i+1][j-1]
                self.d[grid[i-1][j-1]].append(neighbor)
                self.d[grid[i-1][j-1]].append(systemmic)
    def adjacentSum(self, value: int) -> int:
        return self.d[value][0]

    def diagonalSum(self, value: int) -> int:
        # print(self.padding)
        return self.d[value][1]
# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)


# source:https://leetcode.cn/submissions/detail/579237088/ 差分
class MyCalendarThree:

    def __init__(self):
        self.d = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> int:
        self.d[startTime] += 1
        self.d[endTime] -= 1
        ans = res = 0
        for k in sorted(self.d.keys()):
            res += self.d[k]
            ans = max(ans, res)
        # print(ans, sorted(self.d.items()))
        return ans


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)