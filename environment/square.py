import webcolors

class Square:

    def __init__(self, color, value):
        self.squareColor = webcolors.rgb_to_hex((color[0], color[1], color[2]))
        self.squareValue = value
