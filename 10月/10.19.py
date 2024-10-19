# source:https://leetcode.cn/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/description/
from cmath import inf
from collections import defaultdict, deque
from typing import List, Optional


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        flag = 0
        for i in range(len(nums)):
            if not flag:
                if nums[i] == 0:
                    cnt += 1
                    flag = 1
            else:
                if nums[i]^1 == 0:
                    cnt += 1
                    flag = 0
        return cnt

# source:https://leetcode.cn/problems/maximum-candies-you-can-get-from-boxes/description/
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        ans = 0
        q = deque()
        visit = [0 for _ in range(len(status))]
        key = defaultdict(int)
        box = defaultdict(int)
        for v in initialBoxes: # 1e3
            if not visit[v]:
                if (status[v] or key[v]):
                    q.append(v)
                    ans += candies[v]
                    for k in keys[v]:
                        key[k] = 1
                    while q:
                        x = q.popleft()
                        for k in keys[x]:
                            key[k] = 1
                            if key[k] and box[k] and not visit[k]:
                                visit[k] = 1
                                ans += candies[k]  
                                q.append(k)
                        for value in containedBoxes[x]:
                            if not visit[value]:
                                if (status[value] or key[value]):
                                    q.append(value)
                                    visit[value] = 1
                                    ans += candies[value]            
                                else:
                                    box[value] = 1
                else:
                    box[v] = 1
        return ans

# source:https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree/description/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        def create(root, limit):
            if root == limit:
                return None
            if root.next == limit:
                return TreeNode(root.val)
            
            fast = root
            slow = root

            while (fast.next != limit and fast.next.next != limit):
                fast = fast.next.next
                slow = slow.next
            
            node = TreeNode(slow.val)
            node.left = create(root, slow)
            node.right = create(slow.next, limit)
            return node
        return create(head, None)

#source:https://leetcode.cn/problems/network-delay-time/description/ dijkstra
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        value = [[inf for _ in range(n)] for _ in range(n)]
        for i, j, v in times:
            value[i-1][j-1] = v
        
        dis = [inf for _ in range(n)]
        dis[k-1] = 0
        visit = [0 for _ in range(n)]
        
        while 1:
            mn = inf
            index = -1
            for i in range(n):
                if not visit[i]:
                    if mn >= dis[i]:
                        mn = dis[i]
                        index = i
            if index == -1:
                break
            visit[index] = 1
            for i in range(n):    
                dis[i] = min(dis[i], dis[index]+value[index][i])
        
        return max(dis) if max(dis) != inf else -1