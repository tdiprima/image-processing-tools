"""
Count black pixels in an image.
Reads an image, converts it to grayscale, resizes it, and then exits.

https://stackoverflow.com/questions/19167348/count-the-black-pixels-using-opencv/
"""

import cv2
import numpy as np


def cv_size(img):
    return tuple(img.shape[1::-1])


# rgbImage = cv2.imread('../images/prob.png')
rgbImage = cv2.imread('../images/class.png')

grayImage = cv2.cvtColor(rgbImage, cv2.COLOR_BGR2GRAY)

rows, cols = grayImage.shape
print(rows, cols)
resizedImage = cv2.resize(grayImage, np.size(cols / 3, rows / 4), 0, 0, interpolation=cv2.INTER_LINEAR)

exit(0)
