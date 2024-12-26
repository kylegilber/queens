from environment.image import Image

from environment.board import Board

import numpy as np


def player():

    # Initialize helper class instance
    img = Image()

    # Derive color configuration from user image
    colors = img.getSquareColors()
    colors = np.reshape(colors, (9,9))
    colors = colors.transpose()

    # Recreate gameboard
    initialState = Board(colors)
    board = initialState.getSquareValues()
    regions = set()

    if solve(board, colors, regions, 0) == False:
        print("Solution not found")
    else: printBoard(board)


def solve(board, colorGrid, regions, column):

    if column > 8:
        if len(regions) < 9:
            return False
        return True

    for row in range(9):

        if validate(board, row, column):
            
            color = colorGrid[row][column]

            if color not in regions:
                board[row][column] = 1
                regions.add(color)

                if solve(board, colorGrid, regions, column + 1) == True:
                    return True
                
                board[row][column] = 0
                regions.remove(colorGrid[row][column])
    
    return False


def validate(board, row, col):

    # Check row for queens
    if board[row].count(1) > 0: return False
    
    try: # Check upper left diagonal for queen
        if board[row - 1][col - 1] == 1: return False
    except: None
    try: # Check lower left diagonal for queen
        if board[row + 1][col - 1] == 1: return False
    except: None
    try: # Check upper right diagonal for queen
        if board[row - 1][col + 1] == 1: return False
    except: None
    try: # Check lower right diagonal for queen
        if board[row + 1][col + 1] == 1: return False
    except: None

    return True


def printBoard(board):
    """
    Output the current value of the board's squares
    """

    for row in range(9):
        for col in range(9):
            print('|', end=str(board[row][col]))
        print("|", end='\n')


player()