#!/usr/bin/env python

"""
A simple python script to generate a header.
"""

import sys
import cv2
import openslide


def main():
    png = cv2.imread('TCGA-3C-AALI-01Z-00-DX1.png', cv2.IMREAD_COLOR)  # Loads a color image.
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
