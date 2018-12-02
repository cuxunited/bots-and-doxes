import numpy as np

##var
count = 10
dots = 5
length = 7
width = 7
p1point = 0
p2point = 0
##array
grid = np.zeros((length, width))
for i in range(length):
    for j in range(width):
        if i % 2 == 0 and j % 2 == 0:
            grid[i][j] = dots


##loop to play game
while count != 0:
 
    rownum = input()
    colnum = input()
    player = input()

    grid[int(rownum)][int(colnum)]=player
    print(grid)
    print("Moves left:")
    print(count-1)
    count = count-1

    ##square 1
    if grid[0][1] and grid[1][0] and grid[1][2] and grid[2][1] == 1:
        grid[1][1]=player
        print(grid)
        print("Moves left:")
        print(count-1)

    elif grid[0][1] and grid[1][0] and grid[1][2] and grid[2][1] == 2:
        grid[1][1]=player
        print(grid)
        print("Moves left:")
        print(count-1)
       
    ##square 2
    elif grid[2][1] and grid[3][0] and grid[3][2] and grid[4][1] == 1:
            grid[3][1]=input()
            print(grid)
            print("Moves left:")
            print(count-1)

    elif grid[2][1] and grid[3][0] and grid[3][2] and grid[4][1] == 2:
            grid[3][1]=input()
            print(grid)
            print("Moves left:")
            print(count-1)

    ##square 3
    elif grid[4][1] and grid[5][0] and grid[5][2] and grid[6][1] == 1:
        grid[5][1]=input()
        print(grid)
        print("Moves left:")
        print(count-1)

    elif grid[4][1] and grid[5][0] and grid[5][2] and grid[6][1] == 2:
        grid[5][1]=input()
        print(grid)
        print("Moves left:")
        print(count-1)

    ##square 4
    elif grid[0][3] and grid[1][2] and grid[1][4] and grid[2][3] == 1:
        grid[1][3]=input()
        print(grid)
        print("Moves left:")
        print(count-1)

    elif grid[0][3] and grid[1][2] and grid[1][4] and grid[2][3] == 2:
        grid[1][3]=input()
        print(grid)
        print("Moves left:")
        print(count-1)

    ##square 5
    elif grid[2][3] and grid[1][0] and grid[3][4] and grid[4][3] == 1:
        grid[3][6]=input()
        print(grid)
        print("Moves left:")
        print(count-1)

    elif grid[2][3] and grid[1][0] and grid[3][4] and grid[4][3] == 2:
        grid[3][6]=input()
        print(grid)
        print("Moves left:")
        print(count-1)

    ##square 6
    elif grid[4][3] and grid[5][2] and grid[5][4] and grid[6][3] == 1:
        grid[5][3]=input()
        print(grid)
        print("Moves left:")
        print(count-1)

    elif grid[4][3] and grid[5][2] and grid[5][4] and grid[6][3] == 2:
        grid[5][3]=input()
        print(grid)
        print("Moves left:")
        print(count-1)

    ##square 7
    elif grid[0][5] and grid[1][4] and grid[1][6] and grid[2][5] == 1:
        grid[1][5]=input()
        print(grid)
        print("Moves left:")
        print(count-1)


    elif grid[0][5] and grid[1][4] and grid[1][6] and grid[2][5] == 2:
        grid[1][5]=input()
        print(grid)
        print("Moves left:")
        print(count-1)

    ##square 8
    elif grid[2][5] and grid[3][4] and grid[3][6] and grid[4][5] == 1:
        grid[3][5]=input()
        print(grid)
        print("Moves left:")
        print(count-1)

    elif grid[2][5] and grid[3][4] and grid[3][6] and grid[4][5] == 2:
        grid[3][5]=input()
        print(grid)
        print("Moves left:")
        print(count-1)

    ##square 9
    elif grid[4][5] and grid[5][4] and grid[5][6] and grid[6][5] == 1:
        grid[5][5]=input()
        print(grid)
        print("Moves left:")
        print(count-1)

    elif grid[4][5] and grid[5][4] and grid[5][6] and grid[6][5] == 2:
        grid[5][5]=input()
        print(grid)
        print("Moves left:")
        print(count-1)

    elif count == 0:
        break


##point counter

if grid[1][1]== 1:
    p1point= p1point+1 

if grid[3][1]==1:
    p1point= p1point+1 

if grid[5][1]==1:
    p1point= p1point+1 

if grid[1][3]==1:
    p1point= p1point+1 

if grid[3][3]==1:
    p1point= p1point+1 

if grid[5][3]==1:
    p1point= p1point+1 

if grid[1][5]==1:
    p1point= p1point+1 

if grid[3][5]==1:
    p1point= p1point+1 

if grid[5][5]==1:
    p1point= p1point+1 









if grid[1][1]== 2:
    p1point= p1point+1 

if grid[3][1]==2:
    p1point= p1point+1 

if grid[5][1]==2:
    p1point= p1point+1 

if grid[1][3]==2:
    p1point= p1point+1 

if grid[3][3]==2:
    p1point= p1point+1 

if grid[5][3]==2:
    p1point= p1point+1 

if grid[1][5]==2:
    p1point= p1point+1 

if grid[3][5]==2:
    p1point= p1point+1 

if grid[5][5]==2:
    p1point= p1point+1 




##end result
print(grid)
print("Results")
print("Player 1:")
print(p1point+"Points")
print("Player 2:")
print(p2point+"Points")


        
