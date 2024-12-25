# Converts an entire SVS image to PNG after cropping, scaling down, and applying a convolution matrix to it.
# TODO: python test_vips.py input_image.svs output_image.png
import sys

import pyvips as Vips

# "../TCGA-06-0148-GBM.svs" ./outfile.png
im = Vips.Image.new_from_file(sys.argv[1])

mask = Vips.Image.new_from_array([[-1, -1, -1],
                                  [-1, 16, -1],
                                  [-1, -1, -1]], scale=8)

# Then why are we doing this, if it doesn't get cropped?
im = im.crop(100, 100, im.width - 200, im.height - 200)
im = im.similarity(scale=0.9)
im = im.conv(mask)

im.write_to_file(sys.argv[2])
