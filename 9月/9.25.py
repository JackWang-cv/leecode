# source:https://leetcode.cn/problems/naming-a-company/description/ 哈希表 枚举
from collections import defaultdict
from typing import List

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # 将名字按照去掉首字母后的部分进行分组
        groups = defaultdict(set)
        for idea in ideas:
            groups[idea[1:]].add(idea[0])  # 存储首字母

        # 初始化所有首字母的集合
        total_prefixes = defaultdict(set)
        for idea in ideas:
            total_prefixes[idea[0]].add(idea[1:])

        # 计算有效的公司名字数目
        ans = 0
        # 遍历所有可能的首字母组合 (两个不同的首字母)
        for a in range(26):
            for b in range(a + 1, 26):
                prefix_a = chr(a + ord('a'))
                prefix_b = chr(b + ord('a'))

                # 找到以两个首字母开头的名字集合
                set_a = total_prefixes[prefix_a]
                set_b = total_prefixes[prefix_b]

                # 交集的大小是无效的，因为新名字会存在于原ideas中
                common = set_a & set_b

                # 有效的组合是：
                # 在 set_a 中的名字（除去 common 部分） 与 prefix_b 交换
                # 在 set_b 中的名字（除去 common 部分） 与 prefix_a 交换
                valid_count = (len(set_a) - len(common)) * (len(set_b) - len(common))
                ans += valid_count * 2  # 每个组合可以有两种方式（A交换B 或 B交换A）

        return ans

# source:https://leetcode.cn/problems/power-of-four/description/
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (~n+1) == n and n.bit_length() % 2 == 1