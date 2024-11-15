# source:https://leetcode.cn/submissions/detail/580683497/ 双指针
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        ans = 0
        cnt = 0
        for i in range(len(grid)):
            left = 0
            right = len(grid[i])-1
            while left < right:
                if grid[i][left] ^ grid[i][right]:
                    cnt += 1
                left += 1
                right -= 1
        ans = cnt
        cnt -= cnt
        for j in range(len(grid[0])):
            left = 0
            right = len(grid)-1
            while left < right:
                if grid[left][j] ^ grid[right][j]:
                    cnt += 1
                left += 1
                right -= 1
        ans = min(ans, cnt)
        return ans

# source:https://leetcode.cn/submissions/detail/580687786/ 栈
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i, v in enumerate(s):
            if stack == []:
                stack.append([v, 1])
            else:
                if v == stack[-1][0]:
                    stack[-1][1] += 1
                else:
                    stack.append([v, 1])
            if stack[-1][1] == k:
                stack.pop()
        # print(stack)
        ans = ''
        for s, num in stack:
            ans += s*num
        return ans

# source:https://leetcode.cn/submissions/detail/580706204/ 栈
class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0
        stack = []
        for i, v in enumerate(directions):
            if not stack:
                if v != 'L':
                    stack.append(v)
            else:
                # ssl
                if v == 'S':
                    while stack and stack[-1] == 'R':
                        ans += 1
                        stack.pop()
                    stack.append('S')
                elif v == 'R':
                    stack.append(v)
                else:
                    if stack[-1] == 'R':
                        ans += 2
                        stack.pop()
                        while stack and stack[-1] == 'R':
                            ans += 1
                            stack.pop()
                        stack.append('S')
                    elif stack[-1] == 'S':
                        ans += 1
                        stack.append('S')
            # print(stack, ans)
        return ans