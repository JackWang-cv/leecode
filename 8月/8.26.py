# source:https://leetcode.cn/problems/employee-importance/description/

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


from typing import List


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def find(value, ans):
            i = 0
            j = len(employees)-1
            while i <= j:
                mid = (i+j)//2
                if employees[mid].id == value:
                    ans += employees[mid].importance
                    for k in employees[mid].subordinates:
                        if not dist.get(k,0):
                            member.append(k)
                    break
                elif employees[mid].id > value:
                    j = mid-1
                else:
                    i = mid+1
            return ans

        employees.sort(key=lambda x:x.id)
        i = ans = 0
        j = len(employees)-1
        member = []
        dist = {}
        while i <= j:
            mid = (i+j)//2
            if employees[mid].id == id:
                ans += employees[mid].importance
                member = employees[mid].subordinates
                break
            elif employees[mid].id > id:
                j = mid-1
            else:
                i = mid+1
        
        
        for v in member:
            dist[v] = dist.get(v,0)+1
            ans = find(v,ans)
        return ans
        