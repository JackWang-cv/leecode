# source:https://leetcode.cn/problems/implement-trie-prefix-tree/ 字典树
class Node:

    def __init__(self):
        self.son = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.son:
                cur.son[c] = Node()
            cur = cur.son[c]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.son:
                return False
            cur = cur.son[c]
        return cur.end
    
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.son:
                return False
            cur = cur.son[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# source:https://leetcode.cn/submissions/detail/584605939/ 堆+贪心
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        store = []
        record, i = 0, 0
        while i < len(apples) or store:
            if i < len(apples) and apples[i] > 0:
                heapq.heappush(store, [days[i]+i, apples[i]])
            while store and store[0][0] < i+1:
                heapq.heappop(store)
            if store:
                record += 1
                store[0][1] -= 1
                if not store[0][1]:
                    heapq.heappop(store)
            i += 1
        return record