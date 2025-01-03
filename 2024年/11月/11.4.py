# source:https://leetcode.cn/problems/sum-of-distances/ 
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)
        for i, v in enumerate(nums):
            d[v].append(i)
        # print(d)
        total = defaultdict(list)
        for i in d.keys():
            total[i].append(0)
            for v in d[i]:
                total[i].append(total[i][-1]+v)
        # print(total)
        sign = defaultdict(int)
        ans = []
        for i, v in enumerate(nums):
            sign[v] += 1
            # 左右
            res = sign[v]*i - (total[v][sign[v]]) + (total[v][-1] - total[v][sign[v]]) - i * (len(total[v]) - sign[v] - 1)
            ans.append(res)
        return ans

