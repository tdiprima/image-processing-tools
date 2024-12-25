# Extracts the red channel from an image, creates a new, initially empty image of the same size, assigns the extracted red channel to the new image, and saves the new image.
# https://pythonexamples.org/python-opencv-extract-red-channel-of-image/
# To visualize the image in red color, let us make the blue and green components to zeroes.

import cv2
import numpy as np

# read image
src = cv2.imread('cv2-resize-image-original.png', cv2.IMREAD_UNCHANGED)
print(src.shape)

# extract red channel
red_channel = src[:, :, 2]  # G, B, R

# create empty image with same shape as that of src image
red_img = np.zeros(src.shape)

# assign the red channel of src to empty image
red_img[:, :, 2] = red_channel

# save image
cv2.imwrite('cv2-red-channel-1.png', red_img)

exit(0)
