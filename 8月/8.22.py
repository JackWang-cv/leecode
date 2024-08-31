import math
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        t = bin(x)[2:]
        distribute = [0,]*int(math.log2(n)+1)
        i = 0
        for j in range(len(t)-1, -1, -1):
            if t[j] == '0':
                if i >= len(distribute):
                    break
                distribute[i] = pow(2, len(t)-j-1)
                i += 1
        left = len(t)
        
        while i < len(distribute):
            distribute[i] = 1 << left 
            left += 1
            i += 1
        
        res = bin(n-1)[2:]
        ans = x
        for k in range(len(res)-1,-1,-1):
            if res[k]=='1':
                ans += distribute[len(res)-k-1]
        return ans
X = Solution()
X.minEnd(5, 1)