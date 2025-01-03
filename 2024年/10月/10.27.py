# source:https://leetcode.cn/problems/redundant-connection/
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visit = [0 for _ in range(len(edges)+1)]
        ans = [-1, -1]
        dit = defaultdict(list)
        def find(i, j):
            sign = [0 for _ in range(len(edges)+1)]
            sign[i] = 1
            d = deque()
            d.append(i)
            while d:
                x = d.popleft()
                if x == j:
                    return 1
                for v in dit[x]:
                    if not sign[v]:
                        sign[v] = 1
                        d.append(v)
            return 0
        for i, j in edges:
            if visit[i] and visit[j]:
                if find(i, j):
                    ans = [i, j]
                else:
                    dit[i].append(j)
                    dit[j].append(i)
            else:
                if not visit[i]:
                    visit[i] = 1
                if not visit[j]:
                    visit[j] = 1
                dit[i].append(j)
                dit[j].append(i)
        return ans

# source:https://leetcode.cn/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        candy = [0 for _ in range(len(candiesCount)+1)]
        for i in range(len(candiesCount)):
            candy[i+1] = candy[i] + candiesCount[i]
        # print(candy)
        ans = []
        for i, j, k in queries:
            st = candy[i+1]-1
            ft = candy[i] // k
            # print(st, ft)
            if ft <= j <= st:
                ans.append(True)
            else:
                ans.append(False)
        return ans

# source:https://leetcode.cn/problems/binary-subarrays-with-sum/description/
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = l1 = l2 = s1 = s2 = 0
        for j, v in enumerate(nums):
            s1 += v
            s2 += v
            while l1 <= j and s1 > goal:
                s1 -= nums[l1]
                l1 += 1
            while l2 <= j and s2 >= goal:
                s2 -= nums[l2]
                l2 += 1
            # print(l2, l1)
            ans += l2 - l1
        return ans
                