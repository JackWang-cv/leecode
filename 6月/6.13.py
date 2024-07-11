# source:https://leetcode.cn/problems/maximum-elegance-of-a-k-length-subsequence/  分类讨论 贪心

"""
作者：力扣官方题解
链接：https://leetcode.cn/problems/maximum-elegance-of-a-k-length-subsequence/solutions/2807350/zi-xu-lie-zui-da-you-ya-du-by-leetcode-s-mw6g/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


"""
from typing import List


class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key=lambda items:-items[0])
        category = set()
        d = []
        elegant = res = 0
        i = 0
        while i < k:
            if items[i][1] not in category:
                category.add(items[i][1])
            else:
                d.append(items[i][0])
            elegant += items[i][0]
            i += 1
        res = max(res, elegant+(len(category))**2)
        while i < len(items):
            if items[i][1] not in category and len(d)>0:
                x = d.pop()
                elegant += items[i][0]-x
                category.add(items[i][1])
                res = max(res, elegant + (len(category))**2)
            i += 1

        return res