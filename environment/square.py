import webcolors

class Square:
    """
    Representation of an individual square on the Queens' game board
    """

    def __init__(self, color, queen):
        """
        Initialize new square instance.

        :param color: ndarray of rgb values [r,g,b]
        :param queen: 1 if square has a queen on it, 0 otherwise 
        """

        # Convert color from rbg array to hex code string
        self.color = webcolors.rgb_to_hex((color[0], color[1], color[2]))

        # Track whether or not the square holds a queen
        self.value = queen