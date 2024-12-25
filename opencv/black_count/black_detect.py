"""
Detects black pixels in an image and changes them to red.
https://answers.opencv.org/question/57532/unable-to-detect-black-pixels/
"""

import cv2

# second = cv2.imread('../images/second.png')
# second = cv2.imread('../images/prob.png')
second = cv2.imread('../images/class.png')


def turn_pixel_red():
    # B, G, R
    second[i, j, 0] = 0
    second[i, j, 1] = 0
    second[i, j, 2] = 255
    print('here')


for i in range(second.shape[0]):
    for j in range(second.shape[1]):
        # if second[i, j, 0] != 0 and second[i, j, 1] != 0 and second[i, j, 2] != 0:
        # if not (second[i, j, 0] == 0 and second[i, j, 1] == 0 and second[i, j, 2] == 0):
        if second[i, j, 0] == 0 and second[i, j, 1] == 0 and second[i, j, 2] == 0:
            turn_pixel_red()

cv2.imwrite('result.png', second)

exit(0)
