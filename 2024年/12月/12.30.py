# source:https://leetcode.cn/problems/linked-list-in-binary-tree/ 递归
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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def find(nodes, link):
            temp = link.next
            if not temp:
                return True
            ans = False
            if nodes.left and nodes.left.val == temp.val:
                ans |= find(nodes.left, temp)
            if nodes.right and nodes.right.val == temp.val:
                ans |= find(nodes.right, temp)
            return ans

        def search(node):
            if not node:
                return False
            res = False
            if node.val == head.val:
                res |= find(node, head)
            res |= search(node.left)
            res |= search(node.right)
            return res
        return search(root)

# source:https://leetcode.cn/problems/swim-in-rising-water/submissions/590214024/ 二分+BFS
from collections import deque
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        mx = 0
        row, col = len(grid), len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                mx = max(mx, grid[i][j])
        
        def find(value):
            q.clear()
            q.append([0, 0])
            visit = [[0 for _ in range(col)] for _ in range(row)]
            visit[0][0] = 1
            while q:
                x, y = q.popleft()
                if x == row-1 and y == col-1:
                    return True
                for i, j in direction:
                    new_x = x+i
                    new_y = y+j
                    if 0 <= new_x < row and 0 <= new_y < col:
                        if not visit[new_x][new_y] and (grid[new_x][new_y] <= value):
                            visit[new_x][new_y] = 1
                            q.append([new_x, new_y])
            return False

        q = deque()        
        direction = [[1,0],[0,-1],[-1,0],[0,1]]
        i, j = grid[0][0], mx
        while i < j:
            mid = (i+j)//2
            # print(i, j, mid)
            if find(mid):
                j = mid
            else:
                i = mid+1
        return i