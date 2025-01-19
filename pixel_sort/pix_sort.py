"""
Pixel Sorting
Sorting the pixels of an input image by their color values, exporting the sorted pixels data into an Excel file, and creating a video of the pixel sorting process.
TODO: Place the image file (e.g., example.jpg) in a folder named Image in the same directory as the script.
  python3 script_name.py -f example
http://eddiejackson.net/data/python/pixel_sort.py
"""
import argparse
import colorsys  # Conversions between color systems
import math
import os

import cv2
import numpy as np
import pandas as pd
# import sound
from tqdm import tqdm

# Taking arguments from command line
parser = argparse.ArgumentParser()  # you initialize as such
parser.add_argument("-f", required=True, help="enter file name of your picture")
# parser.add_argument("-s", required=True, help="Speed factor of the audio to be increased or decreased")
# parser.add_argument("-av", required=True, help="Speed factor of the audio visualizer to be increased or decreased")

# The add_argument tells you what needs to be given as an input sp its help
args = parser.parse_args()  # you take the arguments from command line

if not os.path.isdir("Image_sort"):
    os.makedirs("Image_sort/" + str(args.f))
    print(str(args.f).capitalize() + " directory is created.")

# Defining all global variables
df = []
total = 0
dict, final, img_list = {}, [], []


def create_dataset(val=0, data=[]):
    """
    Create dataframe and save it as an Excel file
    """
    global dict
    dict[len(data)] = data
    if val != 0:
        if val == max(dict.keys()):
            final_df = pd.DataFrame(dict[val], columns=["Blue", "Green", "Red"])
            final_df.to_excel("Image_sort/" + str(args.f) + "/" + "output.xlsx")


def generate_colors(c_sorted, frame, row):
    """
    Generating colors for each row of the frame
    """
    global df, img_list
    height = 25
    img = np.zeros((height, len(c_sorted), 3), np.uint8)
    for x in range(0, len(c_sorted)):
        r, g, b = c_sorted[x][0] * 255, c_sorted[x][1] * 255, c_sorted[x][2] * 255
        c = [r, g, b]
        df.append(c)
        img[:, x] = c  # the color value for the xth column , this gives the color band
        frame[row, x] = c  # changes added for every row in the frame

    create_dataset(data=df)
    return img, frame


def measure(count, row, col, height, width):
    """
    Measures the total number of pixels that were involved in pixel sort
    """
    global total
    total += count
    if row == height - 1 and col == width - 1:
        create_dataset(val=total)


def step(bgr, repetitions=1):
    """
    Step Sorting Algorithm
    """
    b, g, r = bgr
    # lum is calculated as per the way the humans view the colors
    lum = math.sqrt(.241 * r + .691 * g + .068 * b)

    # conversion of rgb to hsv values
    h, s, v = colorsys.rgb_to_hsv(r, g, b)  # h,s,v is a better option for classifying each color

    # Repetitions are taken to decrease the noise
    h2 = int(h * repetitions)
    v2 = int(v * repetitions)

    # To get a smoother color band
    if h2 % 2 == 1:
        v2 = repetitions - v2
        lum = repetitions - lum

    return h2, lum, v2


def find_threshold(lst, add):
    """
    Threshold set for avoiding extreme sorting of the pixels
    """
    for i in lst:
        add.append(sum(i))
    return (max(add) + min(add)) / 2


def make_video():
    out = cv2.VideoWriter("Image_sort/" + str(args.f) + "/" + str(args.f) + ".mp4", cv2.VideoWriter_fourcc(*'mp4v'), 16,
                          (800, 500))
    for count in tqdm(range(1, 500 + 1)):
        file_name = "Image_sort/" + str(args.f) + "/" + str(count) + ".jpg"
        img = cv2.imread(file_name)
        out.write(img)
        os.remove(file_name)
    out.release()


def main():
    global img_list
    img = cv2.imread("Image/" + str(args.f) + ".jpg")
    img = cv2.resize(img, (800, 500))
    img_list.append(img)

    height, width, _ = img.shape
    print(">>> Row-wise Color sorting")
    for row in tqdm(range(0, height)):
        color, color_n = [], []
        add = []

        for col in range(0, width):
            val = img[row][col].tolist()

            # val includes all rgb values between the range of 0 to 1
            # This makes the sorting easier and efficient
            val = [i / 255.0 for i in val]
            color.append(val)

        thresh = find_threshold(color, add)  # setting the threshold value for every row in the frame

        # For the specific row , if all the values are non-zero then it is sorted with color
        # if np.all(np.asarray(color)) == True:
        if np.all(np.asarray(color)):
            color.sort(key=lambda bgr: step(bgr, 8))  # step sorting
            band, img = generate_colors(color, img, row)
            measure(len(color), row, col, height, width)

        # For the specific row , if any of the values are zero it gets sorted with color_n
        # if np.all(np.asarray(color)) == False:
        if not np.all(np.asarray(color)):
            for ind, i in enumerate(color):
                # Accessing every list within color
                # Added to color_n if any of the element in the list is non-zero
                # and their sum is less than threshold  value

                if np.any(np.asarray(i)) == True and sum(i) < thresh:
                    color_n.append(i)

            color_n.sort(key=lambda bgr: step(bgr, 8))  # step sorting
            band, img = generate_colors(color_n, img, row)
            measure(len(color_n), row, col, height, width)
        cv2.imwrite("Image_sort/" + str(args.f) + "/" + str(row + 1) + ".jpg", img)

    # Writing down the final sorted image
    image_path = "Image_sort/" + str(args.f) + "/" + str(args.f) + ".jpg"
    cv2.imwrite(image_path, img)  # Displaying the final picture
    # cv2.imshow("Sorted Image", image_path)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    print("\n>>> Formation of the Video progress of the pixel-sorted image")
    make_video()
    # TODO: module 'sound' has no attribute 'main'
    # sound.main(args.f)  # Calling the external python file to create the audio of the pixel-sorted image
    print("Done!")
    exit(0)


main()
