# source:https://leetcode.cn/problems/watering-plants/
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res = 0
        temp = capacity
        for i in range(len(plants)):
            if plants[i] <= capacity:
                res += 1
                capacity -= plants[i]
            else:
                res += 2*i+1
                capacity = temp-plants[i]
        return res

