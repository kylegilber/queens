import tkinter as tk
import numpy as np
from tkinter import filedialog
import cv2

class Image:

    def __init__(self):

        # Init root window
        root = tk.Tk()
        root.withdraw() # Hide window

        # Open file dialog for image selection
        self.filepath = filedialog.askopenfilename(
            title= "Select Screenshot",
            filetypes= [("Image files", "*.png;*.jpg;*.jpeg;")])

        # Init adjacency matrix to store color for each square 
        self.squareColors = [[0 for x in range(9)] for y in range(9)]

    def detectSquares(self):

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

        # Find contours in edges
        contours, hierarchy = cv2.findContours(
            image= edges,
            mode= cv2.RETR_TREE,
            method= cv2.CHAIN_APPROX_SIMPLE
        )

        # Parse contours for squares
        for contour in contours:

            epsilon = 0.02 * cv2.arcLength(contour, True)
            possible = cv2.approxPolyDP(contour, epsilon, True)

            if len(possible) == 4:
                cv2.drawContours(image, [possible], -1, (0,255,0), 2)
                cv2.draw

        cv2.imwrite('detectedLines.png', image)


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
            threshold= 5,
            maxLineGap= 175
        )

        # Draw lines on image
        for line in lines:
            x1, y1, x2, y2 = line[0]

            cv2.line(
                img= image,
                pt1= (x1, y1),
                pt2= (x2, y2),
                color= (0, 255, 0),
                thickness= 3
            )

        # Save image
        cv2.imwrite('detectedLines.png', image)
        

i = Image()
i.detectBoard()

