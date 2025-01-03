# source:https://leetcode.cn/problems/minimum-length-of-anagram-concatenation/submissions/588267279/
class Solution:
    def minAnagramLength(self, s: str) -> int:
        for k in range(1, len(s)//2+1):
            if len(s) % k:
                continue
            t = sorted(s[:k])
            if all(t == sorted(s[i:i+k]) for i in range(k, len(s)+1-k,k)):
                return k
        return len(s)

# source:https://leetcode.cn/problems/minimum-number-of-days-to-make-m-bouquets/ 二刷 一刷：7.26
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m*k:
            return -1
        def find(value):
            cnt, temp = 0, 0
            for t in bloomDay:
                if t <= value:
                    temp += 1
                else:
                    temp = 0
                if temp == k:
                    temp = 0
                    cnt += 1
            return cnt >= m

        i, j = min(bloomDay), max(bloomDay)
        while i < j:
            mid = (i+j)//2
            if find(mid):
                j = mid
            else:
                i = mid+1
        return i

# source:https://leetcode.cn/problems/earliest-second-to-mark-indices-i/ 二分
class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        if total+n > len(changeIndices):
            return -1
        def judge(value):
            d.clear()
            for time, v in enumerate(changeIndices[:value]):
                d[v] = time+1
            # print(d)
            if len(d) < len(nums):
                return False
            space, ori = 0, 0
            for v, time in sorted(d.items(), key=lambda x:x[1]):
                # print(index, time)
                space += time - ori -1
                ori = time
                if space - nums[v-1] < 0:
                    return False
                space -= (nums[v-1])
            return True

        d = defaultdict(int)
        i, j = total+n, len(changeIndices)+1
        if i == j:
            return i if judge(i) else -1
        else:
            while i < j:
                mid = (i+j)//2
                if judge(mid):
                    j = mid
                else:
                    i = mid+1
        return i if i <= len(changeIndices) else -1