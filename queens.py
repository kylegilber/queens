from image import Image

import numpy as np


def queens():
    """
    Handle the initialization, solving, and output of the Queens puzzle game
    """

    # Initialize helper class instance
    img = Image()

    # Derive square colors from the provided image
    colors = img.getSquareColors()

    # Reshape the list of colors to match the board layout
    color_config = np.reshape(colors, (9,9))
    color_config = color_config.transpose()

    # Initialize set to store the color of color-regions with a queen
    color_regions = set()

    # Create initial 9x9 game board with no placed queens
    game_board = [[0 for col in range(9)] for row in range(9)]

    # Attempt to solve the Queens puzzle
    if solve(game_board, color_config, color_regions, 0) == False:
        print("Solution not found")
    else:
        printBoard(game_board) 
        img.placeQueensOnImage(game_board)


def solve(board, colors, regions, column):
    """
    Employ backtracking to incrementally determine Queen placements on the board

    :param board: matrix representing queen placement on board
    :param colors: matrix storing the color of each square on board
    :param regions: set containing the color of each region that already has a queen
    :param column: the column to place a queen in

    :returns: boolean indicating if a solution was found
    """

    # Goal check
    if column > 8:
        if len(regions) < 9:
            return False
        return True

    for row in range(9):

        if validate(board, row, column):
            
            color = colors[row][column]
            if color not in regions:

                # Place queen on valid positions
                board[row][column] = 1
                regions.add(color)

                if solve(board, colors, regions, column + 1) == True:
                    return True
                
                # Remove queen from square if it doesn't result in a solution
                board[row][column] = 0
                regions.remove(colors[row][column])
    
    return False


def validate(board, row, col):
    """
    Validate queen placement on square

    :param board: matrix representing queen placement on board
    :param row: row index value to look for square
    :param col: column index value to look for square

    :returns: boolean indicating whether it's valid to place a queen on the square
    """

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


if __name__ == "__main__":
    queens()