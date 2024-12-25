# Creates an image from a numerical list representing RGB color channels, saves the image, then
# displays the image's dimensions and indices of non-zero elements in the list.
# https://stackoverflow.com/questions/45963306/html5-canvas-how-to-get-adjacent-pixels-position-from-the-linearized-imagedata
# https://www.geeksforgeeks.org/convert-python-list-to-numpy-arrays/
# https://stackoverflow.com/questions/2659312/how-do-i-convert-a-numpy-array-to-and-display-an-image
import numpy as np
from PIL import Image

FILENAME = 'my.png'

# initializing list
lst = [
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 240, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 240, 0, 0, 0, 255, 0, 0, 0, 240, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 241, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

# converting list to array
arr = np.array(lst)
# arr = np.array(lst).reshape(5, 5, 3)

# OR -
# arr = np.asarray(lst)

# displaying list
# print("List: ", lst)

# displaying array
# print("Array: ", arr)

# vertical line with blue dot
img = Image.fromarray(arr, 'RGB')
img.save(FILENAME)
img.show()

im = Image.open(FILENAME)
w, h = im.size
print('width: ', w)
print('height:', h)

# get non-zero
var = [i for i, e in enumerate(lst) if e != 0]
print(var)
# non_zero_ind = np.nonzero(arr)
# print(non_zero_ind)

exit(0)
