# source:https://leetcode.cn/problems/closest-room/ 降低复杂度
from sortedcontainers import SortedList
from typing import List
from math import inf

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        # 按房间容量升序排序
        rooms.sort(key=lambda r: r[1])
        q = len(queries)
        ans = [-1] * q
        room_ids = SortedList()
        
        # 按查询的 minSize 降序排序，并保留原索引
        sorted_queries = sorted(enumerate(queries), key=lambda x: -x[1][1])
        j = len(rooms) - 1

        for idx, (preferred_id, min_size) in sorted_queries:
            # 动态更新满足 min_size 的房间集合
            while j >= 0 and rooms[j][1] >= min_size:
                room_ids.add(rooms[j][0])
                j -= 1

            # 如果没有满足条件的房间，返回 -1
            if not room_ids:
                continue

            # 二分查找获取最接近的房间 ID
            pos = room_ids.bisect_left(preferred_id)
            closest_id, closest_diff = -1, inf
            
            # 检查左侧邻居
            if pos > 0:
                left_id = room_ids[pos - 1]
                closest_id, closest_diff = left_id, abs(preferred_id - left_id)
            
            # 检查右侧邻居
            if pos < len(room_ids):
                right_id = room_ids[pos]
                if abs(preferred_id - right_id) < closest_diff:
                    closest_id = right_id

            # 更新答案
            ans[idx] = closest_id

        return ans

# source:https://leetcode.cn/problems/maximum-sum-obtained-of-any-permutation/submissions/587434646/ 差分 
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort()
        mod = pow(10,9)+7
        store = [0 for _ in range(len(nums)+2)]
        for i, j in requests:
            store[i+1] += 1
            store[j+2] += -1
        for i in range(1, len(store)):
            store[i] += store[i-1]
        # print(store)
        ans = 0
        store.sort(reverse=True)
        for v in store:
            if v == 0:
                break
            ans += (v*nums[-1])
            ans %= mod
            nums.pop()
        return ans