# source : https://leetcode.cn/problems/amount-of-time-for-binary-tree-to-be-infected/?envType=daily-question&envId=2024-04-24
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque

class Solution:
    def find_start_node(self, node, start, parent_map, parent=None):
        if node is None:
            return None
        parent_map[node] = parent
        if node.val == start:
            return node
        return self.find_start_node(node.left, start, parent_map, node) or \
               self.find_start_node(node.right, start, parent_map, node)

    def amountOfTime(self, root: TreeNode, start: int) -> int:
        if not root:
            return 0
        parent_map = {}
        start_node = self.find_start_node(root, start, parent_map)
        if not start_node:
            return 0

        queue = deque([start_node])
        visited = set([start_node])
        time = -1

        while queue:
            time += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in (node.left, node.right, parent_map.get(node)):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        return time

# Example Usage
# Construct the tree and use the Solution class to determine infection time.
