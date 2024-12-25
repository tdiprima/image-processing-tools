# This code imports an image, draws a polygon on it, and displays the updated image.
# python opencv-drawing.py
# https://youtu.be/U6uIrq2eh_o
import cv2
import numpy as np

img = cv2.imread('../images/watch.jpg', cv2.IMREAD_COLOR)

# cv2.line(img, (0, 0), (150, 150), (255, 255, 255), 15)  # bgr
# cv2.rectangle(img, (15, 25), (200, 150), (0, 255, 0), 5)
# cv2.circle(img, (100, 63), 55, (0, 0, 255), -1)  # -1 = fill

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255), 3)  # True = Connect final pt to first pt

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
