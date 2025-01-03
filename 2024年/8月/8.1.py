# source:https://leetcode.cn/problems/minimum-size-subarray-sum/ 滑动窗口
from cmath import inf
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = j = 0
        count_sum = 0
        res = inf
        while j < len(nums):
            count_sum += nums[j]
            while count_sum >= target:
                count_sum -= nums[i]
                res = min(res, j-i+1)                
                i += 1
            j += 1
        return res if res != inf else 0

# source:https://leetcode.cn/problems/uOAnQW/description/
class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort()
        res = 0
        odd = []
        even = []
        count = 0
        for i in range(len(cards)-1, len(cards)-1-cnt,-1):
            if cards[i] % 2 == 0:
                even.append(cards[i])
            else:
                odd.append(cards[i])
            count += cards[i]
        if count % 2 == 0:
            return count
        
        if odd:
            t1 = count - min(odd)
            for j in range(len(cards)-1-cnt, -1, -1):
                if cards[j] % 2 == 0:
                    res = t1 + cards[j]
                    break
        if even:
            t2 = count - min(even)
            for j in range(len(cards)-1-cnt, -1, -1):
                if cards[j] % 2 != 0:
                    res = max(res, t2 + cards[j])
                    break
        return res

# source:https://leetcode.cn/problems/longest-substring-without-repeating-characters/ 滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = mx = 0
        t = []
        while j < len(s):        
            while s[j] in t:
                t.remove(t[0])
            t.append(s[j])
            j += 1
            mx = max(len(t), mx)
        return mx

# source: https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        mx = res = 0
        d = ['a' , 'e', 'i', 'o', 'u']
        for i in range(0, k, 1):
            if s[i] in d:
                mx += 1
        res = max(res, mx)
        i = 1
        for j in range(k, len(s), 1):
            if s[i-1] in d:
                mx -= 1
            i += 1

            if s[j] in d:
                mx += 1
            res = max(res, mx)
        return res