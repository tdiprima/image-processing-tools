"""
This one makes the file size smaller while preserving the image.
Opens an image, sorts each row of pixels by their intensity up to the darkest pixel, creates a new image with the sorted
pixels, displays it, and saves the sorted image.
https://levelup.gitconnected.com/pixel-sorting-in-python-62337c078118
"""
from PIL import Image

img = Image.open("red_rock.jpg")
width, height = img.size
pixels = img.load()


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


new_img = Image.new('RGB', (width, height))

# to make a new image, we'll need to convert the data to a list
sorted_pixels = []
for y in range(height):
    for x in range(width):
        sorted_pixels.append(pixels[x, y])
new_img.putdata(sorted_pixels)

# Display images using the show() method.
new_img.show()

new_img.save("red_rock_sorted.jpg")
