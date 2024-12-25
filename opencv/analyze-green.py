# Reads an image, extracts the green channel, calculates and prints its mean and standard deviation, creates a histogram of pixel values in the green channel, and displays it.
import cv2
import numpy as np
import matplotlib.pyplot as plt


def save_image(array):
    # from PIL import Image
    # im = Image.fromarray(array)
    # im.save("pil_mask.png")
    # It's the same:
    import matplotlib.image
    matplotlib.image.imsave('mat_mask.png', array)


def create_mask(channel, thresh):
    # Mask image based on threshold
    masked_image = np.where((channel > 0) & (channel <= thresh), channel, 0)
    image[:, :, 1] = masked_image
    image[:, :, 0] = 0  # Set blue channel to 0
    image[:, :, 2] = 0  # Set red channel to 0

    # Display masked image
    cv2.imshow('Masked Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Load the image
image = cv2.imread('../images/heatmap-E2-A1IG.png')

# Extract the green channel
green_channel = image[:, :, 1]  # OpenCV uses BGR format

mean_value = np.mean(green_channel)
std_deviation = np.std(green_channel)

print("mean_value", mean_value)
print("std_deviation", std_deviation)

# Compute histogram
hist, bins = np.histogram(green_channel.flatten(), bins='auto', range=[0, 256])
# 'auto' lets numpy choose the best bin size

# save_image(image)  # todo: uncomment if you want it

# Plot histogram
plt.figure()
bar_width = bins[1] - bins[0]
plt.bar(bins[:-1], hist, width=bar_width, align='center', color='green')
# plt.bar(bins[:-1], hist, width=bar_width, align='edge', color='green')
# plt.bar(bins[:-1], hist, width=1, align='edge', color='green')
plt.title("Green Channel Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.ylim(0, 40000)  # Set y-axis limits
plt.xlim(0, 100)  # Set x-axis limits to include zero
plt.show()

# Visual confirmation
# print("Histogram values:", hist)
# print("Bin edges:", bins)

# Mask (we already have one; the input)
# thresh = np.argmax(hist) + 1  # This ends up being 1.
# create_mask(green_channel, 100)

exit(0)
