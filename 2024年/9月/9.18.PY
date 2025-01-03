# source:https://leetcode.cn/problems/the-latest-time-to-catch-a-bus/description/二分
from typing import List


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        start = 0
        t = []
        for index, b in enumerate(buses):
            count = 0
            for p in range(start,len(passengers),1):
                if passengers[p] <= b:
                    count += 1
                    start += 1
                    if index == len(buses)-1:
                        t.append(passengers[p])
                else:
                    break
                if count == capacity:
                    break

        temp = t[-1] - 1 if len(t) == capacity else buses[-1]

        while 1:
            flag = True
            i = 0
            j = len(passengers)-1
            while i <= j:
                mid = (i + j)//2
                if passengers[mid] == temp:
                    temp -= 1
                    flag = False            
                    break
                elif passengers[mid] > temp:
                    j = mid-1
                else:
                    i = mid+1
            if flag:
                return temp
