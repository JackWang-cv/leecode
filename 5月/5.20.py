# source:https://leetcode.cn/problems/palindrome-number/ 双指针
class Solution:
    def isPalindrome(self, x: int) -> bool:
        L = list(str(x))
        l = 0
        r = len(L)-1
        flag = True
        while l <= r:
            if L[l] != L[r]:
                flag = False
                break
            l += 1
            r -= 1
        if flag:
            return True
        else:
            return False