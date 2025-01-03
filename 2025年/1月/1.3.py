# source: https://leetcode.com/problems/my-calendar-ii/ 差分
from collections import defaultdict
from sortedcontainers import SortedDict
class MyCalendarTwo:

    def __init__(self):
        self.d = SortedDict()

    def book(self, startTime: int, endTime: int) -> bool:
        self.d[startTime] = self.d.get(startTime, 0)+1
        self.d[endTime] = self.d.get(endTime, 0)-1
        cnt = 0
        for v in self.d.values():
            cnt += v
            if cnt > 2:
                self.d[startTime] -= 1
                self.d[endTime] += 1
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)

# source: https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/ 滑动窗口 贪心
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        def delete(i):
            d[s[i]] -= 1
            if not d[s[i]]:
                del d[s[i]]
        
        i, ans = 0, 0
        store = defaultdict(int)
        d = defaultdict(int)

        for j, v in enumerate(s):
            d[v] += 1
            while len(d) > maxLetters and i <= j:
                delete(i)
                i += 1

            if j-i+1 > minSize:
                delete(i)
                i += 1

            if minSize == j-i+1:
                store[s[i:j+1]] += 1
                ans = max(ans, store[s[i:j+1]])

        # print(store)
        return ans

# source: https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/ 滑动窗口 二刷 一刷 2024.8.16
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        cnt = 0
        for v in nums:
            cnt += 1 if v else 0
        i, j = 0, 0
        one = 0
        ans = inf
        while j < len(nums) + cnt - 1:
            if nums[j % len(nums)]:
                one += 1
            if (j-i+1) > cnt:
                one -= 1 if nums[i] else 0
                i += 1
            if j-i+1 == cnt:
                ans = min(ans, cnt - one)
            j += 1
        return ans if ans < inf else 0
            