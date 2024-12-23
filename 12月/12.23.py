# source:https://leetcode.cn/problems/exam-room/ 有序集合+堆
from sortedcontainers import SortedList
class ExamRoom:

    def __init__(self, n: int):
        def dist(x):
            l, r = x
            return r-l-1 if l == -1 or r == n else (r-l)>>1

        self.ts = SortedList(key = lambda x:(-dist(x), x[0]))
        self.left, self.right = {}, {}
        self.n = n
        self.add((-1, n))

    def seat(self) -> int:
        x = self.ts[0]
        p = (x[0]+x[1])>>1
        if x[0] == -1:
            p = 0
        elif x[1] == self.n:
            p = self.n - 1
        self.delete(x)
        self.add((x[0],p))
        self.add((p, x[1]))
        return p

    def leave(self, p: int) -> None:
        l, r = self.left[p], self.right[p]
        self.delete((l, p))
        self.delete((p, r))
        self.add((l, r))

    def add(self, s):
        self.ts.add(s)
        self.left[s[1]] = s[0]
        self.right[s[0]] = s[1]

    def delete(self, x):
        self.ts.remove(x)
        self.left.pop(x[1])
        self.right.pop(x[0])
    
    

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)

# source:https://leetcode.cn/problems/maximum-points-inside-the-square/ 二分
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        mx = 0
        for index, (i, j) in enumerate(points):
            temp = max(abs(i), abs(j))
            mx = max(mx, temp)
            points[index] = temp

        def judge(value):
            d.clear()
            ans = 0
            nonlocal res
            for i, v in enumerate(points):
                if v <= value and not d[s[i]]:
                    ans += 1
                    d[s[i]] += 1
                elif v <= value and d[s[i]]:
                    return False         
            res = max(ans, res)    
            return True

        d = defaultdict(int)
        res = 0
        i, j = 0, mx
        while i < j:
            mid = (i+j+1)//2
            if judge(mid):
                i = mid
            else:
                j = mid-1
        judge(i)
        return res