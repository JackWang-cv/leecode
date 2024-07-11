# source:https://leetcode.cn/problems/rotting-oranges/description/?envType=daily-question&envId=2024-05-13
from collections import deque
from typing import List

class Solution:
    def find(self,grid,q):
        s = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    q.append([i,j])
                elif grid[i][j] == 1:
                    s = 1
        return s
    def broad(self,grid,q,judge,flag,flag1):
        L = []
        while len(q)>0:
            temp = q.popleft()
            judge[temp[0]][temp[1]] = 1
            for i,j in [[0,1],[1,0],[0,-1],[-1,0]]:
                x = temp[0] + i
                y = temp[1] + j
                if x>=0 and x<len(grid) and y>=0 and y<len(grid[0]) and judge[x][y]==0:
                    judge[x][y] = 1
                    if grid[x][y]==1:
                        L.append([x,y])
                        flag=1
        for i in L:
            q.append(i)
        return flag,flag1

    # 由于你使用了类型提示（type hints），因此需要导入 List 类型才能正确使用它。在类型提示中，List 是一个泛型，用来指定列表的类型。
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        flag = flag1 = 0
        # judge = [[0,]*len(grid[0])]*len(grid) # 为什么会输入judge[0][0] = 1 会一起改 因为你实际上是创建了一个包含相同引用的列表的列表。
        # 这意味着，你实际上创建了一个包含相同子列表引用的列表。这意味着，对其中一个子列表的更改将反映在所有其他子列表上。这样相当于三个子列表都用同一个地址
        # 详情请见地址.py
        judge = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        q = deque()
        s = self.find(grid,q)
        if len(q)==0:
            if s:
                return -1
            else:
                return 0
        while len(q)!=0:
            flag,flag1 = self.broad(grid,q,judge,flag,flag1)
            if flag:
                res += 1
                flag = 0
            else:
                flag1 = 1

            if flag1:
                for i in range(len(grid)):
                    for j in range(len(grid[0])):
                        if grid[i][j]==1 and judge[i][j]==0:
                            return -1
                return res
        return res
A = Solution()
input = [[2,1,1],[1,1,0],[0,1,1]]
print(A.orangesRotting(input))