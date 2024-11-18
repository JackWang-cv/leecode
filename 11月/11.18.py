# source:https://leetcode.cn/problems/image-smoother/ 模拟
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        direction = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                count = 1
                val = img[i][j]
                for l, r in direction:
                    if i+l < 0 or i+l >= m:
                        continue
                    elif j+r < 0 or j+r >= n:
                        continue
                    else:
                        val += img[i+l][j+r]
                        count += 1
                ans[i][j] = val // count
        return ans

# source:https://leetcode.cn/problems/score-of-parentheses/ 栈
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0
        stack = []
        for v in s:
            if stack == []:
                stack.append([v, 0])
            else:
                if v == '(':
                    stack.append([v, 0])
                else:
                    _, value = stack.pop()
                    if stack:
                        if value == 0:
                            stack[-1][1] += value + 1
                        else:
                            stack[-1][1] += value * 2
                    else:
                        ans += max(value * 2, 1)
        return ans