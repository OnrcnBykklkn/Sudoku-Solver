import numpy as nm

board = [[0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [3,8,4,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,2]]
nm.matrix(board)

def is_valid(x,y,num):
    
    if (num in board[x]):
        return False
    
    for i in range(len(board)):
        if num == board[i][y]:
            return False
    
    help_x = (x//3)*3
    help_y = (y//3)*3
    
    for k in range(0,3):
        for j in range(0,3):
            if (board[help_x+k][help_y+j] == num) and (i != x and j != y):
                return False
            
    return True


def solver(board):

    
    for row in range(0,9):
        for column in range(0,9):
            if board[row][column]== 0:
                for num in range(1,10):
                    if (is_valid(row,column,num)):
                        board[row][column] = num
                        solver(board)
                        board[row][column] = 0                
                return
    print(nm.matrix(board))
    input()



    







