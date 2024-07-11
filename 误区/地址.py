grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

judge = [[0,]*len(grid[0])]*len(grid)

# 打印出每个子列表的地址
for sublist, sublist1 in zip(judge,grid):
    print(id(sublist),id(sublist1))

# 正解
sign = [[0,]*3 for _ in range(3)]
print(sign)
