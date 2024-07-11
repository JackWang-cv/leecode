# source:https://leetcode.cn/problems/detect-capital/
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        t = len(word)
        if t == 1:
            return True

        if word[0] <= "Z" and word[1] <= "Z":
            for i in range(2, t):
                if word[i] >= "a":
                    return False
            return True
        elif (word[0] <= "Z" and word[1] >= "a") or (word[0] >= "a" and word[1] >= "a"):
            for i in range(2, t):
                if word[i] <= "Z":
                    return False
            return True

        return False


a = Solution()
print(a.detectCapitalUse("adbc"))
