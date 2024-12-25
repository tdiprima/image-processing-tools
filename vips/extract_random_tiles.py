# Generates four random 512x512 tiles from a specified .svs image file and writes them out as .png files.
# TODO: Make sure the slideName exists.
__author__ = 'tdiprima'

import random

# from gi.repository import Vips
import pyvips as Vips

# Load the input file.
# TCGA-NC-A5HG-01Z-00-DX1 is LUSC
# TCGA-49-AARN-01Z-00-DX1 is LUAD
slideName = "TCGA-02-0001-01Z-00-DX1-gbm"
im = Vips.Image.new_from_file("../" + slideName + ".svs")

N = 4
# Do N random tiles
for x in range(0, N):
    width = im.width
    height = im.height

    print("width: " + str(width))
    print("height: " + str(height))

    size = 512
    left = random.randint(width / 2, width - 500)
    top = random.randint(height / 2, height - 500)

    print("left: " + str(left))
    print("top: " + str(top))

    im1 = im.extract_area(left, top, size, size)

    im1.write_to_file(
        "./" + slideName + "_" + str(left) + "_" + str(top) + "_" + str(size) + "_" + str(
            size) + ".png")

print('Done.')
