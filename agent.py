from environment.image import Image
from environment.board import Board
from collections import defaultdict
import operator


def search():

    # Init helper class instances 
    img = Image()
    board = Board()

    # Recreate daily board from image
    colors = img.detectBoard()
    board.createBoard(colors)

    queue = [(0, board)]
    visited = []

    while queue:
        
        # Find state w/ smallest heuristic
        i = queue.index(min(queue, key= operator.itemgetter(0)))
        state = queue.pop(i)

        # Add state to list of visited states
        visited.append(state[1].getBoard())

        if goalCheck(state[1]):
            print("")


def goalCheck(state):

    # Init queen counter dict
    clr = defaultdict(int)

    # Init queen counter lists 
    row = [0 for x in range(9)]
    col = [0 for x in range(9)]

    board = state.getBoard()
    squares = state.squares

    for i in range(9):      # Col
        for j in range(9):  # Row
            if board[i][j] == 1:
                
                # Get square color
                color = squares[i][j].squareColor

                # Update counters
                clr[color] += 1
                col[i] += 1
                row[j] += 1

    # Convert clr dict to list
    clr = list(clr.items())

    check = True
    for i in range(9):
        if len(clr) < 9:
            check = False
        elif(row[i] != 1 or
           col[i] != 1 or
           clr[i] != 1):        # POSSIBLE MISTAKE
            check = False

    return check
                
search()