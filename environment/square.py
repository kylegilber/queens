import webcolors

class Square:
    """
    Representation of an individual square on the Queens' game board
    """

    def __init__(self, color, queen):
        """
        Initialize new square instance.

        :param color: hexadecimal color code
        :param queen: 1 if square has a queen on it, 0 otherwise 
        """

        self.color = color
        self.value = queen