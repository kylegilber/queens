from environment.square import Square

from collections import defaultdict


class Board:
    """
    Representation of the Queens' game board where each square in the 9x9 grid is an object of class Square.
    """

    def __init__(self, colors):
        """
        Initialize a new 9x9 board instance with no placed queens.

        :param colors: matrix with the hex color code for each square
        """

        self.squares = [[Square(colors[y][x], 0) for y in range(9)] for x in range(9)]
    

    def getSquareValues(self):
        """
        Representation of the game board where each element in the 9x9 grid is a value indicating if the square has a Queen on it.

        :returns: a matrix of square values
        """
        
        return [[self.squares[x][y].value for x in range(9)] for y in range(9)]
    