# source:https://leetcode.cn/problems/couples-holding-hands/ 并查集
from typing import List

class Union:
    def __init__(self, n):
        self.f = list(range(n))
    
    def find(self, x):
        if self.f[x] != x:
            self.f[x] = self.find(self.f[x])
        return self.f[x]
    
    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.f[fx] = fy

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2  # 总共有多少对情侣
        uf = Union(n)  # 并查集大小为对数
        
        # 将情侣的编号合并到同一个组中
        for i in range(0, len(row), 2):
            a, b = row[i] // 2, row[i + 1] // 2
            uf.union(a, b)
        
        # 计算需要的交换次数
        group_count = len(set(uf.find(i) for i in range(n)))  # 不同连通分量数量
        return n - group_count

# source:https://leetcode.cn/problems/largest-number/ 贪心
from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 将 nums 中的数字转换为字符串
        nums = list(map(str, nums))
        
        # 自定义比较函数
        def compare(x, y):
            if x + y > y + x:
                return -1  # x 应该排在 y 前面
            elif x + y < y + x:
                return 1   # y 应该排在 x 前面
            else:
                return 0   # x 和 y 相等
        
        # 按自定义规则排序
        nums.sort(key=cmp_to_key(compare))
        
        # 拼接排序后的结果
        result = ''.join(nums)
        
        # 如果结果以 "0" 开头（比如 [0, 0]），直接返回 "0"
        return result if result[0] != '0' else '0'
