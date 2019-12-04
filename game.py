import random, sys
def board(panel_list):
    '''Make matrix board of random numbers'''
    # list1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    matrix = []
    while panel_list !=[]:
        matrix.append(panel_list[:4])
        panel_list = panel_list[4:]
    return matrix
def zero(board):
    '''function to find where the zero is'''
    empty_space = None
    for x,item in enumerate(board):
        for y,item in enumerate(board):
            if board[x][y] == 0:
                empty_space = (x,y)
    return empty_space
def draw_board(board):
    '''function to draw the board'''
    print('\n\t+-------+-------+-------+-------|')
    for x,item in enumerate(board):
        for y,item in enumerate(board):
            if board[x][y] == 0:
                print('\t|  XX' , end='')
            else:
                 print('\t|  ' + '{:02d}' .format(board[x][y]), end=' ')
        print('\n\t+-------+-------+-------+-------|')
def ask_number(board, num):
    ''' function to ask for the number to move'''
    # num = input('\nplease type the number of the piece to move : ( q ) to quit  ')
    piece = ()
    for i,item in enumerate(board):
        for j,item in enumerate(board):
            if num == board[i][j]:
                piece = (i,j)
    return piece , num
def game():
    '''Run the game logic'''
    panel_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 14, 0, 13, 10, 15, 12]
    matrix = board(panel_list)
    draw_board(matrix)
    empty_space = zero(matrix)
    print(empty_space)
    move = 0
    direction = []
    for num in [12, 15, 14, 11, 10, 14, 15]:
        piece,num = ask_number(matrix,num)
        print(piece, num)
        if(empty_space==(piece[0]-1,piece[1])):
            direction.append("↓")
        if(empty_space==(piece[0]+1,piece[1])):
            direction.append("↑")
        if(empty_space==(piece[0],piece[1]-1)):
            direction.append("→")
        if(empty_space==(piece[0],piece[1]+1)):
            direction.append("←")
        matrix[empty_space[0]][empty_space[1]]=num
        matrix[piece[0]][piece[1]]=0
        empty_space=(piece[0],piece[1])
        move = move +1
        draw_board(matrix)
        print(" ".join(direction))
        print('you have made ',move , 'moves so far ')
        print(2*'\n')
        
if __name__ == '__main__':
    game()