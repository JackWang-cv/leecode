# source:https://leetcode.cn/problems/defuse-the-bomb/
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = [0,]*len(code)
        for i in range(len(code)):
            temp = 0
            j = 0
            if k>0:
                ii = i+1
            else:
                ii = i-1
            while j<abs(k):
                if ii == len(code):
                    ii = 0
                if ii == -1:
                    ii = len(code)-1
                temp += code[ii]
                if k>0:
                    ii += 1
                else:
                    ii -= 1
                j+=1
            result[i] = temp
        return result





