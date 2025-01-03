# source: https://leetcode.cn/problems/distribute-candies-among-children-i/description/


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        store = []
        for i in range(0,limit+1):
            for j in range(0,limit+1):
                for k in range(0,limit+1):
                    if i+j+k==n:
                        store.append([i,j,k])
        return len(store)


