# source:https://leetcode.cn/problems/minimum-operations-to-make-a-special-number/description/ 贪心

from typing import List


class Solution:
    def minimumOperations(self, num: str) -> int:
        find0 = find5 = False
        n = len(num)
        for i in range(n-1, -1, -1):
            if num[i] in ['0', '5']:
                if find0:
                    return n - i - 2 
                if num[i] == '0':
                    find0 = True
                else:
                    find5 = True
            elif num[i] in ['2', '7']:
                if find5:
                    return n - i - 2
        if find0:
            return n-1
        return n

# X = Solution()
# print(f'{X.minimumOperations("24434566670") = }')

# source:https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days/description/ 二分


class Solution1:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(value):
            count = 1
            t = 0
            for w in weights:
                if t+w > value:
                    count += 1
                    t = w
                else:
                    t += w
            return count <= days
        
        i = max(weights)
        j = sum(weights)
        while i<j:
            mid = (i+j)//2
            if check(mid):
                j = mid
            else:
                i = mid+1
        return i

# source:https://leetcode.cn/problems/koko-eating-bananas/description/ 二分
class Solution2:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(value):
            t = 0
            for i in piles:
                t += (i+value)//value if i % value != 0 else i//value
            return t <= h
        i = 1
        j = max(piles)
        while i<j:
            mid = (i+j)//2
            if check(mid):
                j = mid
            else:
                i = mid+1
        return i

# source:https://leetcode.cn/problems/compare-strings-by-frequency-of-the-smallest-character/description/ 二分
class Solution3:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def cal(s):
            count = 0
            t = 'z'
            for i in s:
                if i < t:
                    t = i
                    count = 1
                elif i == t:
                    count += 1
            return count
        
        def insect(v):
            i = 0
            j = len(words)
            while i<j:
                mid = (i+j)//2
                if words[mid] <= v:
                    i = mid+1
                else:
                    j = mid   
            return len(words) - i 

        for i in range(len(words)):
            words[i] = cal(words[i])
        words.sort()
        for i in range(len(queries)):
            queries[i] = cal(queries[i])
            queries[i] = insect(queries[i])

        return queries