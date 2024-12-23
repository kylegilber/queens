from tkinter import filedialog

import tkinter as tk

import numpy as np

import webcolors

import cv2


class Image:
    """
    Process a user-provided screenshot of the Queens' game board.
    """


    def __init__(self):
        """
        Prompt the user to select and input an image of the game board
        """

        # Init root window
        root = tk.Tk()
        root.withdraw() # Hide window

        # Open file dialog for image selection
        self.filepath = filedialog.askopenfilename(
            title= "Select Screenshot",
            filetypes= [("Image files", "*.png;*.jpg;*.jpeg;")])


    def getGridlines(self, positions):
        """
        Filter lines comprising the game board grid

        :param positions: list of positions corresponding to orthogonal lines
        :returns: list of positions corresponding to the lines comprising the game board
        """

        # Remove duplicate positions
        positions = list(set(positions))

        # Sort line positions
        positions = sorted(positions)

        # Calculate distance between consecutive positions
        dists = np.diff(positions)

        # Calculate the mean distance
        spacing = np.mean(dists)

        # Remove nearby positions
        indices = [i for i in range(len(dists)) if dists[i] < spacing]
        return [positions[i] for i in range(len(positions)) if i not in indices]


    def getCentroid(self, horizontalLines, verticalLines):
        """
        Compute the center coordinates for each square on the game board

        :param horizontalLines: list of horizontal gridline positions
        :param verticalLines: list of vertical gridlines positions
        :returns: list of coordinates corresponding to the center of each square
        """

        return [[
            (horizontalLines[i] + horizontalLines[i + 1]) // 2,
            (verticalLines[j] + verticalLines[j + 1]) // 2
            ] for i in range(9) for j in range(9)
        ]


    def getSquareColors(self):
        """
        Derive game board squares and their colors from user-provided image

        :returns: list of hexadecimal color codes
        """

        # Load image from filepath
        image = cv2.imread(self.filepath)

        # Convert image to grayscale
        grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect edges
        edges = cv2.Canny(
            image= grayscale,
            threshold1= 50,
            threshold2= 150,
            apertureSize= 3,
            L2gradient= True
        )

        # Detect lines from edges
        lines = cv2.HoughLinesP(
            image= edges,
            rho= 1,
            theta= np.pi/180,
            threshold= 50,
            maxLineGap= 1000
        )

        xvals = []
        yvals = []

        # Validate lines
        for line in lines:
            x1, y1, x2, y2 = line[0]

            # If line is orthogonal
            if (abs(x2 - x1) < 3 or
                abs(y2 - y1) < 3):

                # If line is horizontal
                if (abs(x2 - x1) >
                    abs(y2 - y1)):
                    yvals.append(y1)
                else: xvals.append(x1)

        horizontalLines = self.getGridlines(yvals)
        verticalLines = self.getGridlines(xvals)

        if(len(horizontalLines) == len(verticalLines)):
            squares = self.getCentroid(horizontalLines, verticalLines)

            colors = []
            for square in squares:
                color = image[square[1], square[0]]
                colors.append(webcolors.rgb_to_hex((color[0], color[1], color[2])))

        return colors

