# source:https://leetcode.cn/problems/number-of-provinces/ dfs
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        sign = defaultdict(int)
        count = 0
        
        def dfs(v):
            sign[v] = 1
            for i in range(len(isConnected[v])):
                if not sign[i] and isConnected[v][i]:
                    dfs(i)
            
        
        for i in range(len(isConnected)):
            if not sign[i]:
                dfs(i)
                count += 1
        return count

# source:https://leetcode.cn/problems/find-the-xor-of-numbers-which-appear-twice/
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        dit = defaultdict(int)
        ans = 0
        for i in nums:
            dit[i] += 1
            if dit[i] > 1:
                ans ^= i
        return ans