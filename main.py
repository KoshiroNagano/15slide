import random, sys
import argparse
import time
import search 


def board(panel_list):
    """Make matrix board of random numbers"""
    # list1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    matrix = []
    while panel_list !=[]:
        matrix.append(panel_list[:4])
        panel_list = panel_list[4:]
    return matrix
def zero(board):
    """function to find where the zero is"""
    empty_space = None
    for x,item in enumerate(board):
        for y,item in enumerate(board):
            if board[x][y] == 0:
                empty_space = (x,y)
    return empty_space
def draw_board(board):
    """function to draw the board"""
    print("\n\t+-------+-------+-------+-------|")
    for x,item in enumerate(board):
        for y,item in enumerate(board):
            if board[x][y] == 0:
                print("\t|  XX" , end="")
            else:
                 print("\t|  " + "{:02d}" .format(board[x][y]), end=" ")
        print("\n\t+-------+-------+-------+-------|")
def ask_number(board, num):
    """ function to ask for the number to move"""
    # num = input("\nplease type the number of the piece to move : ( q ) to quit  ")
    piece = ()
    for i,item in enumerate(board):
        for j,item in enumerate(board):
            if num == board[i][j]:
                piece = (i,j)
    return piece , num
def game(args, panel_list):
    """Run the game logic"""
    num_list = search.a_search(panel_list)
    matrix = board(panel_list)
    draw_board(matrix)
    empty_space = zero(matrix)
    move = 0
    direction = []
    for num in num_list :
        piece,num = ask_number(matrix,num)
        # print(piece, num)
        if(empty_space==(piece[0]-1,piece[1])):
            direction.append("下")
        if(empty_space==(piece[0]+1,piece[1])):
            direction.append("上")
        if(empty_space==(piece[0],piece[1]-1)):
            direction.append("右")
        if(empty_space==(piece[0],piece[1]+1)):
            direction.append("左")
        matrix[empty_space[0]][empty_space[1]]=num
        matrix[piece[0]][piece[1]]=0
        empty_space=(piece[0],piece[1])
        move = move +1
        if args.draw_board:
            draw_board(matrix)
            print(2*"\n")
    print("you have made ",move , "moves so far ")
    print(", ".join(direction))
        
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--draw_board",action="store_true")
    args = parser.parse_args()

    stdin = input("Please type the number of initial state : ")
    if stdin == "1" :
        panel_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 14, 0, 13, 10, 15, 12]
    if stdin == "2" :
        panel_list = [2, 10, 3, 4, 1, 14, 6, 7, 5, 0, 11, 8, 9, 13, 15, 12]
    if stdin == "3" :
        panel_list = [14, 3, 6, 4, 10, 2, 11, 7, 1, 5, 15, 8, 9, 13, 0, 12]
    if stdin == "4" :
        panel_list = [14, 3, 11, 6, 10, 15, 5, 4, 13, 9, 2, 7, 1, 12, 8, 0]
    start = time.time()
    game(args, panel_list)
    elapsed_time = time.time() - start
    print ("elapsed_time: {0}".format(elapsed_time) + "[sec]")