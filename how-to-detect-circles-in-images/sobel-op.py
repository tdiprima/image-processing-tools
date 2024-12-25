"""
Uses the Sobel Operator to detect the edges of a circle in an image and creates a new image with these edges highlighted.
https://www.codingame.com/playgrounds/38470/how-to-detect-circles-in-images
Output is a nice, clean, thick-line circle.
"""
from math import sqrt

from PIL import Image, ImageDraw

# Load image:
input_image = Image.open("input.png")
input_pixels = input_image.load()

# Sobel kernels
kernel_y = [[-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]]
kernel_x = [[-1, -2, -1],
            [0, 0, 0],
            [1, 2, 1]]

# Create output image
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

# Compute convolution between intensity and kernels
for x in range(1, input_image.width - 1):
    for y in range(1, input_image.height - 1):
        mag_x, mag_y = 0, 0
        for a in range(3):
            for b in range(3):
                xn = x + a - 1
                yn = y + b - 1
                intensity = sum(input_pixels[xn, yn]) / 3
                mag_x += intensity * kernel_x[a][b]
                mag_y += intensity * kernel_y[a][b]

        # Draw in black and white the magnitude
        color = int(sqrt(mag_x ** 2 + mag_y ** 2))
        draw.point((x, y), (color, color, color))

output_image.save("sobel-op.png")
