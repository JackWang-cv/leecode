# source:https://leetcode.cn/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/

class Solution:
    def average(self, salary: List[int]) -> float:
        mx = max(salary)
        mn = min(salary)
        res = 0
        for i in salary:
            if (i == mx) or (i == mn):
                continue
            res += i
        return float(res/(len(salary)-2))