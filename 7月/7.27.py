# source:https://leetcode.cn/problems/lexicographically-smallest-string-after-operations-with-constraint/description/ 贪心
class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        d = [chr(x+97) for x in range(26)]
        ans = ''
        for i in s:
            if not k:
                ans += i
                continue
            t1 = ord(i) - 97 - 0
            t2 = 25 + 1 - (ord(i)-97)
            # print(t1 , t2, k)
            if t1 <= t2 and t1 <= k:
                k -= t1
                ans += d[0]
            elif t1 <= t2 and t1 > k:
                ans += d[t1-k]
                k = 0
            elif t1 > t2 and t2 <= k:
                k -= t2
                ans += d[0]
            elif t1 > t2 and t2 > k:
                ans += d[t1-k]
                k = 0
        return ans

# source:https://leetcode.cn/problems/maximum-candies-allocated-to-k-children/description/
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        def check(v):
            count = 0
            for c in candies:
                count += c//v
            # print(count, k ,v)
            return count >= k
        
        i = 1
        j = max(candies)
        while i < j:
            # print(i, j)
            mid = (i+j+1)//2
            if check(mid):
                i = mid
            else:
                j = mid-1
        return i

# source:https://leetcode.cn/problems/online-election/description/ 二分
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        tops = []
        voteCounts = defaultdict(int)
        voteCounts[-1] = -1
        top = -1
        for p in persons:
            voteCounts[p] += 1
            if voteCounts[p] >= voteCounts[top]:
                top = p
            tops.append(top)
        self.tops = tops
        self.times = times
        
    def q(self, t: int) -> int:
        l, r = 0, len(self.times) - 1
        # 找到满足 times[l] <= t 的最大的 l
        while l < r:
            m = l + (r - l + 1) // 2
            if self.times[m] <= t:
                l = m
            else:
                r = m - 1
        # 也可以使用内置的二分查找的包来确定 l
        # l = bisect.bisect(self.times, t) - 1
        return self.tops[l]
    

