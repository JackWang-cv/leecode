# source:https://leetcode.cn/problems/minimum-cost-for-cutting-cake-ii/ 堆+贪心
class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        store = []
        heapq.heapify(store)
        for i, v in enumerate(horizontalCut):
            heapq.heappush(store, [-1*v, 0, i])
        for i, v in enumerate(verticalCut):
            heapq.heappush(store, [-1*v, 1, i])
        row, col = 1, 1
        cost = 0
        while store:
            num, direction, index = heapq.heappop(store)
            cost += -1*num * (col if direction == 0 else row)
            if direction:
                col += 1
            else:
                row += 1
        return cost
    
# source：https://leetcode.cn/problems/split-array-largest-sum/ 二刷 一刷 7.11
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        i, j = max(nums), sum(nums)
        def find(value):
            total ,cnt = 0, 1
            for v in nums:
                if total + v <= value:
                    total += v
                else:
                    total = v
                    cnt += 1
            return cnt > k
        
        while i < j:
            mid = (i+j)//2
            if find(mid):
                i = mid+1
            else:
                j = mid
        return i

# source:https://leetcode.cn/problems/minimized-maximum-of-products-distributed-to-any-store/submissions/589238289/ 二刷 一刷 7.30
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        i, j = 1, max(quantities)

        def find(value):
            cnt = 0
            for v in quantities:
                cnt += v//value if v % value == 0 else v//value+1
            # print(cnt, value)
            return cnt > n
        
        while i < j:
            mid = (i+j)//2
            if find(mid):
                i = mid+1
            else:
                j = mid
        return i