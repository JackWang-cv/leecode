# source:https://leetcode.cn/problems/maximize-the-confusion-of-an-exam/description/ 滑窗
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def find(s):
            i = j = 0
            mx = 0
            dj = []
            while j<len(answerKey):
                while len(dj) == k and answerKey[j] == s:
                    i = dj[0]+1
                    dj.remove(dj[0])
                if answerKey[j] == s:
                    dj.append(j)
            # print(i, j)
                mx = max(mx, j - i+1)
                j += 1
            return mx
          
        res = 0
        res = max(res, find('F'))
        res = max(res, find('T'))
        return res

