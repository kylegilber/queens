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
    

    def __lt__(self, other):
        """
        Compare Board objects based on their heuristic value

        :param other: a Board class object
        :returns: whether the first Board object's heuristic value is less than the second
        """

        return self.heuristic() < other.heuristic()


    def getSquareValues(self):
        """
        Representation of the game board where each element in the 9x9 grid is a value indicating if the square has a Queen on it.

        :returns: a matrix of square values
        """
        
        return tuple(tuple(self.squares[x][y].value for x in range(9)) for y in range(9))
    

    def groupByColor(self):
        """
        Group the squares on the board by color.

        :returns: a dictionary where keys are hex color codes, and values are lists with the values of every square of that color.
        """

        colors = defaultdict(list)
        for col in range(9):
            for row in range(9):
                square = self.squares[col][row]
                colors[square.color].append(square.value)

        return colors


    def heuristic(self):
        """
        Compute the 'distance' a Board state is from the goal state

        :returns: the amount of rows, columns, and color blocks that do not have exactly one queen
        """

        values = self.getSquareValues()
        colors = self.groupByColor()
        incorrectRows = sum(1 for col in range(9) if values[col].count(1) != 1)
        incorrectCols = sum(1 for row in zip(*values) if row.count(1) != 1)
        incorrectClrs = sum(1 for row in list(colors.keys()) if colors[row].count(1) != 1)

        return incorrectRows + incorrectCols + incorrectClrs


    def printBoard(self):
        """
        Output the current value of the board's squares
        """

        for row in range(9):
            for col in range(9):
                print('|', end=str(self.squares[row][col].value))
            print("|", end='\n')