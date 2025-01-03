# source:https://leetcode.cn/problems/account-balance-after-rounded-purchase/

class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        t = purchaseAmount % 10
        if t==0:
            return 100 - purchaseAmount
        elif t<5:
            return 100-(purchaseAmount-t)
        else:
            return 100-(purchaseAmount-t+10)