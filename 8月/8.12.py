# source:https://leetcode.cn/problems/grumpy-bookstore-owner/description/ 滑窗
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        res = count = 0
        for i,v in enumerate(grumpy):
            if not v:
                count += customers[i]
        i = j = 0
        while j < len(grumpy):
            if j-i+1 > minutes:
                if grumpy[i]:
                    count -= customers[i]
                i += 1
                
            if grumpy[j]:
                count += customers[j]
            # print(count)
            res = max(res, count)
            j += 1     
        return res

# source:https://leetcode.cn/problems/implement-magic-dictionary/description/ 
class MagicDictionary:

    def __init__(self):
        self.d = dict([])

    def buildDict(self, dictionary: List[str]) -> None:
        for v in dictionary:
            if len(v) not in self.d.keys():
                self.d[len(v)] = [v]
            else:
                self.d[len(v)].append(v)
        
    def search(self, searchWord: str) -> bool:
        length = len(searchWord)
        if length not in self.d.keys():
            return False
        for v in self.d[length]:
            count = 0
            for i,k in enumerate(searchWord):
                if k == v[i]:
                    count += 1
            if count == length-1:
                return True
        return False



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)

# source:https://leetcode.cn/problems/frequency-of-the-most-frequent-element/submissions/ 滑窗
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = 1
        res = 1
        consume = 0
        while j < len(nums):
            t = nums[j] - nums[j-1]
            while consume + (j-i)*t > k and i < j:
                consume -= (nums[j-1]-nums[i])
                i += 1
            consume += (j-i)*t
            res = max(res,j-i+1)
            j += 1
        return res