# SOURCE:https://leetcode.cn/problems/find-subarray-with-bitwise-or-closest-to-k/description/ 滑窗+栈
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = inf
        bottom = left = right_or = 0
        for right, x in enumerate(nums):
            right_or |= x
            while left <= right and (right_or | nums[left]) > k:
                ans = min(ans, (right_or | nums[left]) - k)
                if bottom <= left:
                    for i in range(right-1, left, -1):
                        nums[i] |= nums[i+1]
                    right_or = 0        
                    bottom = right
                left += 1
            if left <= right:
                ans = min(ans, k - (right_or | nums[left]))
        return ans

# source:
# s会到1e4比较大，会超时
# class Solution:
#     def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
#         ans = []
#         dst = int(s, 2)
#         dst_length = max(dst.bit_length(), 1)
#         zero = len(s) - dst_length
#         for i, j in queries:
#             key = (i ^ j)
#             if key == 0 and s[0] == '0':
#                 ans.append([0,0])
#                 continue
#             key_length = max(key.bit_length(), 1)
#             k = dst_length - key_length
#             count = 0
#             while k >= 0:
#                 if ((dst >> k) ^ key) & (pow(2, key_length)-1) == 0:
#                     ans.append([count + zero, count + key_length-1 + zero])
#                     break
#                 k -= 1
#                 count += 1
#             if k < 0:
#                 ans.append([-1, -1])
#         return ans
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n, m = len(s), {}
        if (i := s.find('0')) >= 0:
            m[0] = (i, i)

        for l, c in enumerate(s):
            if c == '0':
                continue
            x = 0
            # 只需要计算每一个子字符串最多长度30 而不用计算所有子字符串，故不会超时
            for r in range(l, min(l + 30, n)):
                x = (x << 1) | (ord(s[r]) & 1)
                if x not in m:
                    m[x] = (l, r)

        NOT_FOUND = (-1, -1)
        return [m.get(x ^ y, NOT_FOUND) for x, y in queries]

