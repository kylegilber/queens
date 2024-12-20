from environment.image import Image


img = Image()
colors = img.detectBoard()
print(len(colors))