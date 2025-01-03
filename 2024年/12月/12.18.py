# source:https://leetcode.cn/problems/minimum-absolute-sum-difference/ 二分 7.23一刷
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        mx = [0, 0]
        
        MOD = pow(10, 9)+7
        store = []
        for i, v in enumerate(nums1):
            store.append(abs(v-nums2[i]))
        total = sum(store) % MOD
        ans = total
        nums1.sort()
        for index, v in enumerate(nums2):
            i = 0
            j = len(nums1)
            while i<j:
                mid = (i+j)//2
                if nums1[mid] >= v:
                    j = mid
                else:
                    i = mid+1

            if i == len(nums1):
                ans = min(ans, (total - store[index] + abs(nums1[-1]-v)))
            elif i == 0:
                ans = min(ans, (total - store[index] + abs(nums1[0]-v)))
            else:
                mn = min(abs(nums1[i-1]-v), abs(nums1[i]-v))
                ans = min(ans, (total - store[index] + mn))
            # print(total, ans)
        return ans % MOD

# source:https://leetcode.cn/problems/online-election/submissions/587804327/ 二分 7.27 一刷
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        # t时刻谁赢了
        self.top = [-1]
        d = defaultdict(int)
        for i in range(len(persons)):
            d[persons[i]] += 1
            if d[persons[i]] >= d[self.top[-1]]:
                self.top.append(persons[i])
            else:
                self.top.append(self.top[-1])
            self.time = times
    def q(self, t: int) -> int:
        i = 0
        j = len(self.time)
        while i < j:
            mid = (i+j)//2 
            if self.time[mid] <= t:       
                i = mid+1
            else:
                j = mid
        # print(i, self.top)
        return self.top[i]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)