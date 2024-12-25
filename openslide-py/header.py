"""
A simple python script to generate a header.
Loads a color image and an OpenSlide object, then it prints the dimensions of the
image and the OpenSlide object, along with predetermined patch dimensions.
"""

import sys

import cv2
# https://pypi.org/project/openslide-python/
# python3.9 -m pip install --upgrade pip
# python3.9 -m pip install openslide-python
# or: pip3 install openslide-python
import openslide


def main():
    png = cv2.imread('../../images/TCGA-3C-AALI-01Z-00-DX1.png', cv2.IMREAD_COLOR)  # Loads a color image.
    h_png = png.shape[0]
    w_png = png.shape[1]

    slide = openslide.OpenSlide('TCGA-3C-AALI-01Z-00-DX1.svs')
    width = slide.dimensions[0]
    height = slide.dimensions[1]

    obj = {"img_width": str(width),
           "img_height": str(height),
           "patch_w": str(200),
           "patch_h": str(200),
           "png_w": str(w_png),
           "png_h": str(h_png)}

    print(obj)


if __name__ == '__main__':
    sys.exit(main())
