# source:https://leetcode.cn/problems/minimum-rectangles-to-cover-points/description/ 贪心
from typing import List


class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        count = 1
        last = -1
        for i, _ in sorted(points, key = lambda x:x[0]):
            if last == -1:
                last = i
            else:
                if i - last > w:
                    count += 1
                    last = i
        return count


# source:https://leetcode.cn/problems/combination-sum/description/ 递归
class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def dfs(i: int, left: int) -> None:
            if left == 0:
                # 找到一个合法组合
                ans.append(path.copy())
                return

            if left < candidates[i]:
                return

            # 枚举选哪个
            for j in range(i, len(candidates)):
                path.append(candidates[j])
                dfs(j, left - candidates[j])
                path.pop()  # 恢复现场

        dfs(0, target)
        return ans            
    
# source:https://leetcode.cn/problems/furthest-building-you-can-reach/description/ 贪心+堆
from heapq import heappush, heappop

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb > 0:
                heappush(heap, climb)
            if len(heap) > ladders:
                bricks -= heappop(heap)
            if bricks < 0:
                return i
        return len(heights) - 1