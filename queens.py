from image import Image
import numpy as np
import random

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
        print_board(game_board) 
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


def print_board(board):
    """
    Output the current value of the board's squares
    """

    for row in range(9):
        for col in range(9):
            print('|', end=str(board[row][col]))
        print("|", end='\n')


def generate_color_regions():
    """
    Generate a random configuration of 9 color-regions on the board
    using a flood-fill expansion from randomly placed seeds

    :returns: 9x9 matrix where each cell value indicates its color region
    """

    colors = np.full((9, 9), -1, dtype=np.int8)

    # Randomly select 9 seed cells
    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)
    seeds = cells[:9]
 
    # Assign each seed a unique color
    for color, (r, c) in enumerate(seeds):
        colors[r, c] = color
    
    unassigned = set(cells[9:])

    # Designate seeds as static (single-cell, never expand)
    num_static = random.choices([0, 1, 2, 3], weights=[50, 30, 15, 5])[0]
    static = set(random.sample(range(9), num_static))
    
    # Non-static cells whose neighbors haven't been expanded yet
    frontier = [seed for i, seed in enumerate(seeds) if i not in static]

    NEIGHBORS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while unassigned:
        next_frontier = []
        for (r, c) in frontier:
            for (dr, dc) in NEIGHBORS:
                nr, nc = r + dr, c + dc
                if (nr, nc) in unassigned:
                    colors[nr, nc] = colors[r, c]
                    unassigned.remove((nr, nc))
                    next_frontier.append((nr, nc))
        frontier = next_frontier if next_frontier else list(unassigned)

    return colors

if __name__ == "__main__":
    queens()