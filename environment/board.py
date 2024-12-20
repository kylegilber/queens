from square import Square

class Board:

    def __init__(self):
        self.gameTiles = [[0 for x in range(9)] for y in range(9)]

    def createBoard(self):
        for row in range(9):
            for col in range(9):
                self.gameTiles[row][col] = Square(None, 0)

    def printBoard(self):
        print("hello")
        for row in range(9):
            for col in range(9):
                print('|', end=str(self.gameTiles[row][col].squareValue))
            print("|", end='\n')