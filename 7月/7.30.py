# source:https://leetcode.cn/problems/double-modular-exponentiation/
from typing import List


class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i in range(len(variables)):
            a = variables[i][0]
            b = variables[i][1]
            c = variables[i][2]
            d = variables[i][3]

            if target >= d:
                continue
            temp = (a**b - (a**b // 10) * 10) % 10
            temp = pow(temp, c)
            temp %= d
            if temp == target:
                res.append(i)            
        return res

# source:https://leetcode.cn/problems/maximum-value-at-a-given-index-in-a-bounded-array/description/ 二分+贪心
# 这道题贪心的点在于二分后使得该值最大，那么其他应该依次递减，不能比原数值大或者相等
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def check(v, left, right, count):
            if left+1 < v:
                count += (v-index+v-1)*index//2
            else:
                ones = index+1-v
                count += (1+v-1)*(v-1)//2 + ones

            if right-index+1 < v:
                count += (v-(right-index)+v-1)*(right-index)//2
            else:
                ones = right-index+1-v
                count += (1+v-1)*(v-1)//2 + ones
            return count <= maxSum

            # 暴力会超时
            # print(v, left, right, count)
            # if left == 0 and right == n-1:
            #     return count <= maxSum
            # elif count > maxSum:
            #     return False
            # flag = False
            # scope = [v-1, v, v+1] if v != 1 else [v, v+1]
            # for s in scope:
            #     if left:
            #         flag = flag or check(s, left-1, right, count+s)
            #     for s1 in scope:
            #         if right != n-1:
            #             flag = flag or check(s, left, right+1, count+s1)
            # return flag

        i = 1
        j = maxSum

        while i < j:
            mid = (i+j+1)//2
            if check(mid, index, n-1, mid):
                i = mid
            else:
                j = mid-1
        return i

# source:https://leetcode.cn/problems/minimized-maximum-of-products-distributed-to-any-store/description/
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def check(v):
            count = 0
            for i in quantities:
                count +=  i//v if i % v == 0 else i//v + 1
            return count > n
        i = 1
        j = max(quantities)
        while i < j:
            mid = (i+j)//2
            if check(mid):
                i = mid + 1
            else:
                j = mid
        return i