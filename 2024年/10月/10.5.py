# source:https://leetcode.cn/problems/maximum-xor-for-each-query/
from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        pre = 0
        ans = []
        for v in nums:
            pre ^= v
            for key in range(2**maximumBit-1, -1, -1):
                if pre ^ key < 2**maximumBit:
                    ans.append(pre ^ key)
                    break
        return ans[::-1]

# source:https://leetcode.cn/problems/neighboring-bitwise-xor/
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ori = 1
        t = ori
        for i in range(len(derived)-1):
            t ^= derived[i]
        return t ^ ori == derived[-1]