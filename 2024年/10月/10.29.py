# source:https://leetcode.cn/problems/subarray-sum-equals-k/
from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x

        ans = 0
        cnt = defaultdict(int)
        for v in s:
            ans += cnt[v - k]
            cnt[v] += 1
        return ans

# source:https://leetcode.cn/problems/number-of-sub-arrays-with-odd-sum/
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # 哈希表记录奇偶个数
        total = [0 for _ in range(len(arr)+1)]
        for i, v in enumerate(arr):
            total[i+1] = total[i] + v
        cnt = [0 for _ in range(len(total)+1)]
        for i, v in enumerate(total):
            if v & 1:
                cnt[i+1] = cnt[i] + 1
            else:
                cnt[i+1] = cnt[i]
        ans = 0
        total_num = len(total)
        # print(total)
        # print(cnt)
        for i in range(1, len(total)):
            if total[i] & 1:
                ans += i - cnt[i]
            else:
                ans += cnt[i]
        return ans % (pow(10, 9)+7)

# source:https://leetcode.cn/problems/subarray-sums-divisible-by-k/
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # 哈希表存模后值
        total = [0 for _ in range(len(nums)+1)]
        for i, v in enumerate(nums):
            total[i+1] = total[i] + v
        cnt = defaultdict(int)
        ans = 0
        print(total)
        for v in total:
            ans += cnt[v % k]
            cnt[v % k] += 1
            # print(cnt, ans)
        return ans

# source:https://leetcode.cn/problems/continuous-subarray-sum/description/
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = [0 for _ in range(len(nums)+1)]
        for i, v in enumerate(nums):
            total[i+1] = total[i] + v
        d = defaultdict(int)
        for i, v in enumerate(total):
            if i >= 2:
                d[total[i-2] % k] = 1
                if d[v % k]:
                    return True
        return False