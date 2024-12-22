from tkinter import filedialog

import tkinter as tk

import numpy as np

import webcolors

import cv2


class Image:
    """
    
    """


    def __init__(self):

        # Init root window
        root = tk.Tk()
        root.withdraw() # Hide window

        # Open file dialog for image selection
        self.filepath = filedialog.askopenfilename(
            title= "Select Screenshot",
            filetypes= [("Image files", "*.png;*.jpg;*.jpeg;")])


    def detectLines(self, pos):

        # Remove duplicate positions
        pos = list(set(pos))

        # Sort line positions
        pos = sorted(pos)

        # Calculate distance between consecutive positions
        dists = np.diff(pos)

        # Calculate the mean distance
        spacing = np.mean(dists)

        # Remove nearby positions
        indices = []
        for i in range(len(dists)):
            if dists[i] < spacing:
                indices.append(i)

        # Update position list
        coords = []
        for i in range(len(pos)):
            if i not in indices:
                coords.append(pos[i])
        
        return coords


    def detectSquares(self, rows, cols):

        # Compute the center coords of each square
        squares = []
        for i in range(len(rows) - 1):
            for j in range(len(cols) - 1):
                squares.append([
                    int(np.mean((rows[i], rows[i+1]))),
                    int(np.mean((cols[j], cols[j+1])))
                ])
        
        return squares


    def detectBoard(self):

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

        rowLines = self.detectLines(yvals)
        colLines = self.detectLines(xvals)

        if(len(rowLines) ==
           len(colLines)):
            squares = self.detectSquares(rowLines, colLines)

            colors = []
            for square in squares:
                color = image[square[1], square[0]]
                colors.append(webcolors.rgb_to_hex((color[0], color[1], color[2])))

        return colors

