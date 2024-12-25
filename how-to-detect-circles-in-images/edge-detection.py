"""
Detects edges in an image by converting it to grayscale and performing convolution operation, then saves the resulting image.
https://www.codingame.com/playgrounds/38470/how-to-detect-circles-in-images
Output is a nice, clean circle.

You could try using Pillow instead, which is a PIL fork:
pip install Pillow
OR:
View | Tool Windows | Python Packages
"""
from math import sqrt

import numpy as np
from PIL import Image, ImageDraw

# Load image:
input_image = Image.open("input.png")
input_pixels = input_image.load()
width, height = input_image.width, input_image.height

# Create output image
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

# Convert to grayscale
intensity = np.zeros((width, height))
for x in range(width):
    for y in range(height):
        intensity[x, y] = sum(input_pixels[x, y]) / 3

# Compute convolution between intensity and kernels
for x in range(1, input_image.width - 1):
    for y in range(1, input_image.height - 1):
        mag_x = intensity[x + 1, y] - intensity[x - 1, y]
        mag_y = intensity[x, y + 1] - intensity[x, y - 1]

        # Draw in black and white the magnitude
        color = int(sqrt(mag_x ** 2 + mag_y ** 2))
        draw.point((x, y), (color, color, color))

output_image.save("edge.png")
