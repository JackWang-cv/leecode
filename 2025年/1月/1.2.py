# source: https://leetcode.com/problems/my-calendar-i/ 二分
class MyCalendar:

    def __init__(self):
        self.store = []

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.store:
            self.store.append((startTime, endTime))
            return True
        
        temp = sorted(self.store, key=lambda x:x[0])
        i, j = 0, len(temp)
        while i < j:
            mid = (i+j)//2
            if temp[mid][1] <= startTime:
                i = mid+1
            else:
                j = mid
   
        if i < len(temp) and endTime > temp[i][0]:
            return False
        self.store.append((startTime, endTime))
        return True