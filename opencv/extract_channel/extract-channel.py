# Extracts the red channel from an image and writes it to a new greyscale image.
# https://pythonexamples.org/python-opencv-extract-red-channel-of-image/
import cv2

# read image
src = cv2.imread('cv2-resize-image-original.png')
print(src.shape)

# extract red channel
red_channel = src[:, :, 2]  # G, B, R

# write red channel to greyscale image
cv2.imwrite('cv2-red-channel.png', red_channel)

exit(0)
