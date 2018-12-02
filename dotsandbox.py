import numpy as np

count=33
dots = 5
length = 7
width = 7
grid = np.zeros((length, width))
for i in range(length):
    for j in range(width):
        if i % 2 == 0 and j % 2 == 0:
            grid[i][j] = dots

while count != 0:
 
    rownum = input()
    colnum = input()

    if grid[0][1] == 0:
        grid[int(rownum)][int(colnum)]=input()
        print(grid)
        print("moves left:")
        print(count)
        count = count-1

    elif grid[0][1] and grid[1][0]:
        grid[int(rownum)][int(colnum)]=7

    elif count == 0:
        break

print(grid)
print("moves left:")
print(count)
        
