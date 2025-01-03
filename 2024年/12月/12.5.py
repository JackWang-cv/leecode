# source:https://leetcode.cn/problems/minimum-moves-to-capture-the-queen/ 枚举
class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:

        if a != e and b != f:
            pass
        else:
            if a != e:
                temp_a = a
                while temp_a != e:
                    temp_a += -1 if temp_a > e else 1
                    if temp_a == c and b == d:
                        break
                else:
                    return 1
            else:
                temp_b = b
                while temp_b != f:
                    temp_b += -1 if temp_b > f else 1
                    if temp_b == d and a == c:
                        break
                else:
                    return 1

        if abs(c - e) == abs(d - f):
            while c != e:
                c += -1 if c > e else 1
                d += -1 if d > f else 1
                if c == a and d == b:
                    break
            else:
                return 1
        return 2

# source:https://leetcode.cn/problems/design-add-and-search-words-data-structure/submissions/585280482/ 字典树
class Node():
    def __init__(self):
        self.son = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for i, c in enumerate(word):
            if c not in cur.son.keys():
                cur.son[c] = Node()
            cur = cur.son[c]
        cur.end = True

    def dfs(self, node, word):
        for i, c in enumerate(word):
            if c == '.':
                if i != len(word)-1:
                    ans = False
                    for v in node.son.keys():
                        ans |= self.dfs(node.son[v], word[i+1:])
                    return ans
                else:
                    for k in node.son.keys():
                        if node.son[k].end:
                            return True
                    else:
                        return False
            else:
                if c not in node.son.keys():
                    return False
                node = node.son[c]
        return node.end

    def search(self, word: str) -> bool:
        cur = self.root
        return self.dfs(cur, word)
                

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)