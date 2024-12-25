# Compares two images to check if they are identical and handles exceptions if they're not.
from PIL import Image
from PIL import ImageChops


def equal(im1, im2):
    return ImageChops.difference(im1, im2).getbbox() is None


img = Image.open('default.png')
# img = Image.open("/Users/tdiprima/Documents/matlab/2021/images/my.png")
img1 = Image.open('renderByProb.png')

try:
    equal(img, img1)
except ValueError as err:
    print("Value error:", err)
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
