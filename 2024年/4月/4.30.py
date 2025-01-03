# source: https://leetcode.cn/problems/number-of-employees-who-met-the-target/

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ans = 0
        for i in hours:
            if i >= target:
                ans+=1
        return ans