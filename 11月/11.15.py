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
# 这段代码实现了计算车辆碰撞次数的功能
# 使用栈来模拟车辆移动和碰撞的过程:
# - 如果栈为空且当前车辆不是向左移动(L),则将其入栈
# - 如果当前车辆静止(S):
#   - 将所有向右移动(R)的车辆弹出并计数碰撞次数
#   - 最后将S入栈
# - 如果当前车辆向右移动(R):
#   - 直接入栈
# - 如果当前车辆向左移动(L):
#   - 如果栈顶是R,计数2次碰撞,弹出R
#   - 继续弹出所有R并计数碰撞
#   - 最后将S入栈
#   - 如果栈顶是S,计数1次碰撞,将S入栈
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