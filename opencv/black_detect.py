"""
Detects black pixels in an image and changes them to red.
https://answers.opencv.org/question/57532/unable-to-detect-black-pixels/
"""

import cv2
import numpy as np

# Load the image
second = cv2.imread('../images/second.png')

if second is None:
    raise ValueError("Image not found or unable to load. Check the file path.")

# Ensure the image is in the correct format (BGR)
if len(second.shape) < 3 or second.shape[2] != 3:
    raise ValueError("Expected a color image with 3 channels (BGR).")

# Convert all black pixels (0, 0, 0) to red (0, 0, 255)
# Create a mask for black pixels
black_pixels_mask = np.all(second == [0, 0, 0], axis=-1)

# Set the black pixels to red
second[black_pixels_mask] = [0, 0, 255]

# Save the result
cv2.imwrite('result.png', second)

print("Processing complete. Result saved as 'result.png'.")
