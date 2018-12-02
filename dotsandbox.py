import numpy as np

dot = "Q"
length = 7
width = 7
grid = np.zeros((length, width))
for i in range(length):
    for j in range(width):
        if i % 2 == 0 and j % 2 == 0:
            grid[i][j] = 5

rownum = input()
colnum = input()
grid[int(rownum)][int(colnum)]=1






print(grid)

