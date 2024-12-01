# source:https://leetcode.cn/problems/minimum-ascii-delete-sum-for-two-strings/ dp LCS
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        f = [[0]*(n2+1) for _ in range(n1+1)]
        for i, v in enumerate(s2):
            f[0][i+1] = ord(v) + f[0][i]
        
        for i, v in enumerate(s1):
            f[i+1][0] = f[i][0] + ord(v)
            for j, c in enumerate(s2):
                if v == c:
                    f[i+1][j+1] = f[i][j]
                else:
                    f[i+1][j+1] = min(f[i][j+1] + ord(v), f[i+1][j] + ord(c))

        return f[-1][-1]

# source:https://leetcode.cn/problems/total-cost-to-hire-k-workers/ 堆
from collections import deque
import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans = 0
        n = len(costs)
        if candidates < len(costs)/2:
            q = deque()
            temp1 = costs[:candidates]
            temp2 = costs[n-candidates:]
            q = deque(costs[candidates:n-candidates])
            heapq.heapify(temp1)
            heapq.heapify(temp2)
            for _ in range(k):
                if not temp1:
                    res2 = heapq.heappop(temp2)
                    ans += res2
                    continue
                elif not temp2:
                    res1 = heapq.heappop(temp1)
                    ans += res1
                    continue
                res1 = heapq.heappop(temp1)
                res2 = heapq.heappop(temp2)
                if res1 <= res2:
                    ans += res1
                    if q:
                        heapq.heappush(temp1, q.popleft())
                    heapq.heappush(temp2, res2)
                else:
                    ans += res2
                    if q:
                        heapq.heappush(temp2, q.pop())
                    heapq.heappush(temp1, res1)
        else:
            temp = costs
            heapq.heapify(temp)
            for _ in range(k):
                ans += heapq.heappop(temp)
        return ans 