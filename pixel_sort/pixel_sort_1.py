"""
This one makes a mess of the image, like it's supposed to.
Opens an image, sorts the pixels in each row from darkest to brightest, then creates and displays a new image from the sorted pixels, saving it with a new name.
https://levelup.gitconnected.com/pixel-sorting-in-python-62337c078118
"""
from PIL import Image


def sort_row(row):
    min_ = 255 * 3  # I guess to make sure that the first min is always larger.
    min_index = 0
    # find the darkest pixel in the row
    for i in range(len(row)):
        # each pixel has an RGB value, for instance (255, 255, 255)
        temp = row[i][0] + row[i][1] + row[i][2]
        if temp < min_:
            min_ = temp
            min_index = i
    # sort the row up the brightest pixel
    sorted_row = row[:min_index]
    sorted_row.sort()

    return sorted_row + row[min_index:]


def pixel_sort():
    print("loading the image...")
    # load the image data
    img = Image.open("red_rock.jpg")
    # load the pixel data from the file.
    pixels = img.load()
    width, height = img.size

    print("sorting the image...")

    # loop through each row and sort the pixels in that row
    for y in range(height):
        # get a row
        row = []
        for x in range(width):
            row.append(pixels[x, y])
            # sort the row
            row = sort_row(row)
        # record the sorted data
        for x in range(width):
            pixels[x, y] = row[x]

    # to make a new image, we'll need to convert the data to a list
    sorted_pixels = []
    for y in range(height):
        for x in range(width):
            sorted_pixels.append(pixels[x, y])

    new_img = Image.new('RGB', (width, height))
    new_img.putdata(sorted_pixels)
    # Display images using the show() method.
    new_img.show()

    # save the file with a new name.
    new_img.save("red_rock_sorted.jpg")


pixel_sort()
