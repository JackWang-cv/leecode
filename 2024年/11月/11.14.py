# source:https://leetcode.cn/submissions/detail/580426316/ dfs 哈希表
from collections import defaultdict
from typing import List


class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        def dfs(node):
            if d[node] == []:
                return 0
            ans = 0
            last = -1
            for v in d[node]:
                if not vit[v]:
                    vit[v] = True
                    count[v] = dfs(v)
                    if last==-1:
                        last = count[v]
                    elif last != count[v]:
                        sign[node] = True
                    ans += count[v] +1
            return ans
        cnt = 0
        d = defaultdict(list)
        count = defaultdict(int)
        sign = defaultdict(bool)
        vit = defaultdict(bool)
        for i, j in edges:    
            d[i].append(j)    
            d[j].append(i)
        vit[0] = True
        dfs(0)
        # print(count)
        # print(sign)
        for k in d.keys():
            if sign[k] == False:
                cnt += 1
        return cnt

# source:https://leetcode.cn/submissions/detail/580441040/ 栈 
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0 for _ in range(n)]
        stack = []
        for s in logs:
            num, sign, time = s.split(':')
            num, time = int(num), int(time)
            if sign == 'start':    
                stack.append([time, 0])
            else:
                start, uesd = stack.pop()    
                ans[num] += time - start + 1 - uesd
                if stack:
                    stack[-1][1] += time - start + 1            
        return ans

# source:https://leetcode.cn/submissions/detail/580447242/ 栈 贪心
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        delete = 0
        i = 0
        while i < len(nums)-1:
            if (i - delete)%2 == 0 and nums[i] == nums[i+1]:
                delete += 1
            i += 1
        if (len(nums)-delete) % 2 != 0:
            delete += 1
        return delete
            