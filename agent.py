from environment.image import Image
from environment.board import Board

img = Image()
board = Board()

colors = img.detectBoard()
board.createBoard(colors)
print(board.squares[0][1].squareColor)
print(board.squares[0][2].squareColor)


