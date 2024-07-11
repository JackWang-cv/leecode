from typing import List


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        res = []
        i = 0
        j = len(nums) - 1

        def judge(k):
            print(k, res)
            t = nums[k]
            if t == 1:
                return False
            elif t == 2:
                res.append(k)
                return True
            else:
                for n in range(2, t):
                    if t % n == 0:
                        return False
                res.append(k)
                return True
        flag1 = flag2 = True
        while flag1 or flag2:
            if flag1 and judge(i) == 0:
                i += 1
            else:
                flag1 = False
            if flag2 and judge(j) == 0:
                j -= 1
            else:
                flag2 = False

        return abs(res[-1]-res[0])


S = Solution()
print(S.maximumPrimeDifference([4,2,5,9,3]))