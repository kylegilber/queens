from environment.square import Square

class Board:

    def __init__(self):
        self.squares = [[0 for x in range(9)] for y in range(9)]

    def createBoard(self, colors):
        i = 0
        for row in range(9):
            for col in range(9):
                self.squares[row][col] = Square(colors[i], 0)
                i += 1

    def getBoard(self):
        return [[self.squares[x][y].squareValue for x in range(9)] for y in range(9)]


    def printBoard(self):
        for row in range(9):
            for col in range(9):
                print('|', end=str(self.squares[row][col].squareValue))
            print("|", end='\n')