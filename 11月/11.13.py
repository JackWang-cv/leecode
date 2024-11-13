# source:https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-ii/submissions/580185415/ 前缀和 滑窗
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        total_0 = [0 for _ in range(len(s)+1)]
        total_1 = [0 for _ in range(len(s)+1)]
        for i, v in enumerate(s):
            if v == '0':
                total_0[i+1] = total_0[i] + 1
                total_1[i+1] = total_1[i]
            else:
                total_0[i+1] = total_0[i]
                total_1[i+1] = total_1[i] + 1
        sign = [True for _ in range(len(s))]
        res = [0 for _ in range(len(s)+1)]
        right = [len(s)]*(len(s))
        i = 0
        # print(total_0)
        # print(total_1)
        for j in range(1, len(total_0)):
            while total_0[j] - total_0[i] > k and total_1[j] - total_1[i] > k:
                right[i] = j-1
                i += 1              
            res[j] = res[j-1] + j-i

        ans = []
        for i, j in queries:
            r = min(right[i], j+1)
            extra = (r-i+1)*(r-i)//2
            # print(r, extra)
            ans.append(res[j+1]-res[r]+extra)
        return ans
# [0, 1, 3, 6, 10, 15, 20, 26]
# [5, 7, 7, 7, 7, 7, 7]

# source:https://leetcode.cn/submissions/detail/580147501/ 堆栈
class CustomStack:

    def __init__(self, maxSize: int):
        self.length = 0
        self.maxsize = maxSize
        self.stack = []
        self.deduce = []

    def push(self, x: int) -> None:
        if self.length < self.maxsize:
            self.length += 1
            self.stack.append(x)
            self.deduce.append(0)
    def pop(self) -> int:
        if self.stack:
            self.length -= 1
            x = self.stack.pop()
            y = self.deduce.pop()
            # 输出
            return x + y
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if k > len(self.deduce):
            for i in range(len(self.deduce)):
                self.deduce[i] += val
        else:
            for i in range(k):
                self.deduce[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)