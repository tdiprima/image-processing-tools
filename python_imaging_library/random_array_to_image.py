# Creates a 256x256 image with random RGB values and saves it as 'myimg.png'.
import random

import numpy as np
from PIL import Image

# Example: 2D Array
width = 256
height = 256
cols = width
rows = height

# Declare 2D array
arr = np.zeros((cols, rows))

# Initialize 2D array values
for i in range(cols):
    for j in range(rows):
        x = random.randint(0, 255)
        # print(x)
        arr[i, j] = str(x)

img = Image.fromarray(arr, 'RGB')
img.save('myimg.png')
img.show()
