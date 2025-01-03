# source:https://leetcode.cn/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/ 贪心
from cmath import inf
from collections import defaultdict, deque
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                ans += 1
        return ans if nums[-2] and nums[-1] else -1

# source:
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        d = defaultdict(list)
        for i in range(n-1, 0, -1):
            d[i].append(i-1)
        q = deque()
        res = inf
        for i, j in queries:
            visit = [0 for _ in range(n)]
            d[j].append(i)
            q.clear()
            q.append([n-1,0])
            while q:
                x, dis = q.popleft()
                visit[x] = 1
                if x == 0:
                    ans.append(min(dis, res))
                    break
                for v in d[x]:
                    if not visit[v]:
                        q.append([v, dis+1])
        return ans

# source:https://leetcode.cn/problems/get-watched-videos-by-your-friends/description/
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        dit = defaultdict(list)
        for i, node in enumerate(friends):
            dit[i] = node
        visit = [0 for _ in range(len(friends))]
        q = deque()
        q.append([id, 0])
        visit[id] = 1
        cnt = defaultdict(int)
        while q:
            x, level_ = q.popleft()
            if level_ > level:
                break
            elif level_ == level:
                for s in watchedVideos[x]:
                    cnt[s] += 1
            for v in dit[x]:
                if not visit[v]:
                    visit[v] = 1
                    q.append([v, level_+1])
        
        res = sorted(cnt.items(), key=lambda x:x[1])
        ans = []
        ans_ = []
        last_c = res[0][1]
        for i, c in res:
            if last_c != c:
                last_c = c
                ans_.sort()
                ans += ans_
                ans_.clear()
            ans_.append(i)
        if ans_:
            ans_.sort()
            ans += ans_
        return ans