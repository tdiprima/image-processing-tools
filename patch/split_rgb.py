#!/usr/bin/python
# python pil image split to rgb
# https://stackoverflow.com/questions/51325224/python-pil-image-split-to-rgb
# https://stackoverflow.com/questions/13550376/pil-image-to-array-numpy-array-to-array-python

import csv

import cv2 as cv
import numpy as np
from PIL import Image

FILENAME = 'TCGA-4Z-AA7Q-01Z-00-DX1.png'


def separate_colors():
    # takes an RGB image, and creates the pixel data for each band by suppressing the bands we don't want.
    img = Image.open(FILENAME)
    data = img.getdata()

    # Suppress specific bands (e.g. (255, 120, 65) -> (0, 120, 0) for g)
    r = [(d[0], 0, 0) for d in data]
    g = [(0, d[1], 0) for d in data]
    b = [(0, 0, d[2]) for d in data]

    img.putdata(r)
    img.show()
    # img.save('r.png')
    img.putdata(g)
    # img.save('g.png')
    img.show()
    img.putdata(b)
    # img.save('b.png')
    img.show()


def use_opencv(filename):
    img = cv.imread(filename)
    b, g, r = cv.split(img)

    print('g.shape', g.shape)
    w, h = g.shape
    data = np.zeros((w, h, 3), dtype=np.uint8)

    for y in range(h):
        for x in range(w):
            data[x, y] = g[x, y]  # we're making it grayscale

    print('data.shape', data.shape)
    img = Image.fromarray(data, 'RGB')
    img.show()

    # # (channel_b, channel_g, channel_r) = cv.split(img)
    # (channel_b, channel_g, channel_r) = (img[:, :, 0], img[:, :, 1], img[:, :, 2])
    # # print(channel_r[0])
    # print(channel_r.shape)  # col, row
    # plt.imshow(channel_r)
    # plt.show()


def use_pil(filename):
    pil_image, data = read_image(filename)
    print('size', pil_image.size)

    lst = separate_rgb(data)
    len_list = len(lst)
    print('List length ' + str(len_list))

    red, green, blue = pil_image.split()
    red.show()
    green.show()
    blue.show()

    if len_list == 3:
        # save_csv(lst[0], 'r')
        # save_csv(lst[1], 'g')
        # save_csv(lst[2], 'b')
        save_image(pil_image, lst[0], 'r')
        save_image(pil_image, lst[1], 'g')
        save_image(pil_image, lst[2], 'b')


def read_image(filename):
    im = Image.open(filename)
    list_of_pixels = list(im.getdata())
    return im, list_of_pixels


def separate_rgb(data):
    # Suppress specific bands (e.g. (255, 120, 65) -> (0, 120, 0) for g)
    r = [(d[0], 0, 0) for d in data]
    g = [(0, d[1], 0) for d in data]
    b = [(0, 0, d[2]) for d in data]

    lst = [r, g, b]
    return lst


def save_image(original_img, list_of_pixels, name):
    im2 = Image.new(original_img.mode, original_img.size)
    im2.putdata(list_of_pixels)
    im2.save(name + '.png')
    return


def save_csv(list_of_pixels, width, name):
    with open(name + '.csv', mode='w') as color_file:
        color_writer = csv.writer(color_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        color_writer.writerow(['"dummy_width":85600, "dummy_height:65000", "dummy_patch_w":200, "dummy_patch_h":200'])
        color_writer.writerow(['i', 'j', 'TIL', 'cancer', 'tissue'])

        idx = color_to_index(name)
        for pix in list_of_pixels:
            print(pix[idx])


def color_to_index(argument):
    switcher = {
        'r': 0,
        'g': 1,
        'b': 2
    }
    return switcher.get(argument, "nothing")


def index_to_color(argument):
    switcher = {
        0: 'r',
        1: 'g',
        2: 'b'
    }
    return switcher.get(argument, "nothing")


def image2pixelarray(filepath):
    """
    Parameters
    ----------
    filepath : str
        Path to an image file

    Returns
    -------
    list
        A list of lists which make it simple to access the greyscale value by
        im[y][x]
    """
    im = Image.open(filepath).convert('L')
    (width, height) = im.size
    greyscale_map = list(im.getdata())
    greyscale_map = np.array(greyscale_map)
    greyscale_map = greyscale_map.reshape((height, width))
    return greyscale_map


def jpg_image_to_array(image_path):
    """
    Loads JPEG image into 3D Numpy array of shape
    (width, height, channels)
    """
    with Image.open(image_path) as image:
        im_arr = np.fromstring(image.tobytes(), dtype=np.uint8)
        im_arr = im_arr.reshape((image.size[1], image.size[0], 3))
    return im_arr


def jpg_image_to_array1(image_path):
    '''
    Use numpy.fromiter to invert a greyscale
    :param image_path:
    :return:
    '''
    im = Image.load('foo.jpg')
    im = im.convert('L')

    arr = np.fromiter(iter(im.getdata()), np.uint8)
    arr.resize(im.height, im.width)

    arr ^= 0xFF  # invert
    inverted_im = Image.fromarray(arr, mode='L')
    inverted_im.show()


def jpg_image_to_array2(image_path):
    """
    Use the tobytes function of the Image object.
    After some timing checks this is much more efficient.
    """
    with Image.open(image_path) as image:
        im_arr = np.fromstring(image.tobytes(), dtype=np.uint8)
        im_arr = im_arr.reshape((image.size[1], image.size[0], 3))
    return im_arr


def test(im):
    list(im.getdata())

    # or, if the image is too big to load entirely into memory,
    # do something like that:

    for pixel in iter(im.getdata()):
        print(pixel)


def mysplit(some_image):
    '''
    Why does red.show() shows image in greyscale instead of red scale?
    All the split channels are simply the value of that specific channel, so they all appear as greyscale when displayed.
    :param some_image:
    :return:
    '''
    pil_image = Image.fromarray(some_image)
    red, green, blue = pil_image.split()
    red.show()


# use_opencv(FILENAME)
use_pil(FILENAME)
# separate_colors()
