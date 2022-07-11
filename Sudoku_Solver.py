# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 22:11:02 2022
Sudoku Solver using Backtracking
@author: Anderson Machado
"""
#if dokusan is not installed, please use the line bellow to install
#pip install dokusan
from dokusan import generators


def generateSudoku():
    #generates a string with the 81 numbers for sudoku,
    board_str = str(generators.random_sudoku(avg_rank=150))
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
           board[i][j] = int(board_str[9*i + j]) 
    
    return board
    

def print_board(board):
    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print("------------------------")
        
        for j in range(len(board[0])):
            if j%3 == 0 and j != 0:
                print(" | ", end="")
            
            if j==8:
                print(board[i][j])
            else:
                print((str(board[i][j])+ " "),end="")
        

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)    # row, col
    return None

def valid_play(board, num, pos):
    #check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box 3x3
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True
        

def solve(board):
    
    empty_pos = find_empty(board)
    if not empty_pos:
        return True
    else:
        row, col = empty_pos
    
    for i in range(1,10):
        if valid_play(board, i, (row, col)):
            board[row][col] = i
            
            if solve(board):
                return True
            
            board[row][col] = 0
    
    return False



def main():
    sudoku_board = generateSudoku()
    print_board(sudoku_board)
    print("-----------SOLVED SUDOKU----------")
    solve(sudoku_board)
    print_board(sudoku_board)



if __name__ == "__main__":
    main()
