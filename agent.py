from environment.image import Image
from environment.board import Board
from collections import defaultdict
import operator
import numpy as np


def search():

    # Initialize helper class instance
    img = Image()

    # Derive color configuration from user image
    colors = img.detectBoard()
    colors = np.reshape(colors, (9,9))

    # Recreate gameboard
    startState = Board(colors)

    queue = [(0, startState)]
    visited = []

    while queue:
        
        # Find state with smallest heuristic
        i = queue.index(min(queue, key= operator.itemgetter(0)))
        state = queue.pop(i)[1]
        board = state.values

        # Add state to visited list
        visited.append(board)

        # Output solution if found
        if heuristic(state) == 0: return state.printBoard()

        #for child in fringe(state[1]):


def heuristic(state):

    values = state.values
    colors = state.groupByColor()

    # Calculate 'distance' from goal state
    incorrectRows = sum(1 for col in range(9) if values[col].count(1) != 1)
    incorrectCols = sum(1 for row in zip(*values) if row.count(1) != 1)
    incorrectClrs = sum(1 for row in list(colors.keys()) if colors[row].count(1) != 1)

    return incorrectRows + incorrectCols + incorrectClrs

search()