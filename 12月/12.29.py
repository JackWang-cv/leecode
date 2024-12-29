# source:https://leetcode.cn/problems/rank-teams-by-votes/ 比较，模拟 
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        ans = ''
        store = [defaultdict(int) for _ in range(len(votes[0]))]
        count = [defaultdict(set) for _ in range(len(votes[0]))]
        for i in range(len(votes)):
            for ind, v in enumerate(votes[i]):
                store[ind][v] += 1

        for i in range(len(store)):
            for s, cnt in sorted(store[i].items(), key=lambda x:-x[1]):
                count[i][cnt].add(s)
        # print(count)

        def mn(i, total):
            if i == len(store):
                return min(total)
            mx = -1
            temp = set()
            for s in total:
                if store[i][s] > mx:
                    mx = store[i][s]
                    temp.clear()
                    temp.add(s)
                elif store[i][s] == mx:
                    temp.add(s)
            if len(temp) == 1:
                return temp.pop()
            else:
                r = mn(i+1, temp)
                return r

        def find(i):
            nonlocal ans
            d = store[i]
            for s, cnt in sorted(d.items(), key=lambda x:-x[1]):
                if s in ans or d[s] == 0:
                    del d[s]
                    continue
                if len(count[i][d[s]]) > 1:
                    search = set()
                    for v in count[i][d[s]]:
                        if v not in ans:
                            search.add(v)
                    s = mn(i+1, search)
                ans += s
                del d[s]
                return 
        
        i = 0
        while i < len(store):
            find(i)
            if not store[i]:
                i += 1
        return ans