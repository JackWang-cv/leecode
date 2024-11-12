# source:https://leetcode.cn/submissions/detail/579855686/ 栈
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 0
        ans = []
        k = 1
        while i < len(target):
            # stack.append(k)
            ans.append('Push')
            if k != target[i]:
                ans.append('Pop')
            else:
                i += 1
            k += 1
        return ans