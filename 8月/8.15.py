# source:https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/description/
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        i = j = 0
        res = count = 0
        total = sum(cardPoints)
        while j < len(cardPoints):
            count += cardPoints[j]
            if len(cardPoints) - (j-i+1) < k:
                count -= cardPoints[i]
                i += 1
            if len(cardPoints) - (j-i+1) == k:
                res = max(res, total - count)
            j += 1
        return res

# source:https://leetcode.cn/problems/trapping-rain-water/description/ 栈
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = list()
        n = len(height)
        
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                ans += currWidth * currHeight
            stack.append(i)
        
        return ans

x = Solution()
print(x.trap([4,3]))
