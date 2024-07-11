# source:https://leetcode.cn/problems/find-longest-special-substring-that-occurs-thrice-ii/
# 比昨天增加了数据测试量，按照昨天方法会出现内存不够用。需要改进，通过不断更新cnt来找到最大相同字符串长度

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        cnt = [[0] * 3 for _ in range(26)]

        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            index = ord(s[i]) - ord('a')
            length = j - i
            if length > cnt[index][0]:
                cnt[index][0], cnt[index][1], cnt[index][2] = length, cnt[index][0], cnt[index][1]
            elif length > cnt[index][1]:
                cnt[index][1], cnt[index][2] = length, cnt[index][1]
            elif length > cnt[index][2]:
                cnt[index][2] = length
            i = j

        res = 0
        for vec in cnt:
            res = max(res, vec[0] - 2, min(vec[0] - 1, vec[1]), vec[2])
        return res if res != 0 else -1