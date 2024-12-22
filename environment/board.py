from environment.square import Square

class Board:

    def __init__(self):
        self.squares = [[0 for x in range(9)] for y in range(9)]

    def createBoard(self, colors):
        i = 0
        for col in range(9):
            for row in range(9):
                self.squares[col][row] = Square(colors[i], 0)
                i += 1

    def getValueBoard(self):
        return [[self.squares[x][y].value for x in range(9)] for y in range(9)]
    
    '''
    def getColorBoard(self):
        
        for col in range(9):
            for row in range(9):
    '''


    def printBoard(self):
        for row in range(9):
            for col in range(9):
                print('|', end=str(self.squares[row][col].value))
            print("|", end='\n')