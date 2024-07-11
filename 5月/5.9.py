# source :https://leetcode.cn/problems/watering-plants-ii/
class Solution:
    def fun(self, L, ca, cb, left, right, res, capacityA, capacityB):
        if (left == right):
            if ca < cb:
                if cb < L[right]:
                    res += 1
                return res
            else:
                if ca < L[left]:
                    res += 1
                return res
        else:
            if ca < L[left]:
                res += 1
                ca = capacityA - L[left]
            else:
                ca -= L[left]
            if cb < L[right]:
                res += 1
                cb = capacityB - L[right]
            else:
                cb -= L[right]
            if left + 1 == right:
                return res
        return self.fun(L, ca, cb, left + 1, right - 1, res, capacityA, capacityB)

    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        res = 0
        return self.fun(plants, capacityA, capacityB, 0, len(plants) - 1, res, capacityA, capacityB)
