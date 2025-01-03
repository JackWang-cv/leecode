# source:https://leetcode.cn/problems/bitwise-and-of-numbers-range/ 位运算
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = left
        i = 0
        while res >> i:
            if (res >> i) & 1 and (res >> (i+1)) & 1 == 0:
                # 判断下一个大的数
                temp = (res >> (i+1)) << (i+1)
                if (temp | (1 << i+1)) <= right:
                    res >>= i+1
                    res <<= i+1
            i += 1
        return res

# source:https://leetcode.cn/problems/implement-magic-dictionary/ 并查集
class Node:
    def __init__(self):
        self.son = {}
        self.end = False

class MagicDictionary:

    def __init__(self):
        self.root = Node()        

    def add(self, words):
        cur = self.root
        for word in words:
            if word not in cur.son.keys():
                cur.son[word] = Node()
            cur = cur.son[word]
        cur.end = True

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
           self.add(word)

    def judge(self, cur, words):
        for v in words:
            if v not in cur.son.keys():
                return False
            cur = cur.son[v]
        return cur.end

    def search(self, searchWord: str) -> bool:
        cur = self.root
        sign = False
        for i, c in enumerate(searchWord):
            for v in cur.son.keys():
                if v != c:
                    sign |= self.judge(cur.son[v], searchWord[i+1:])
            if c not in cur.son.keys():
                break
            cur = cur.son[c]
        return sign

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)