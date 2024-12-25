## Detecting Motion with OpenCV

### How to detect and analyze moving objects with OpenCV

<!-- https://towardsdatascience.com/image-analysis-for-beginners-creating-a-motion-detector-with-opencv-4ca6faba4b42 -->

We're detecting movement!

Motion detection has many purposes. You can use it to start recording once you see movement on a wildlife camera or a security camera, e.g. Another application is performance-improvement. Instead of analyzing a whole image, we only have to work with small parts that moved. Like only identifying the color of the moving cars in the image above.

In this article, we'll create a fully working motion detector that can be used for all of the use-cases above. In the process, we'll learn a lot about processing images with OpenCV. At the end of this article, you'll have a fully operational motion detector and a lot more knowledge about image processing. Let's code!

## Series

This article is part of a series about OpenCV image processing. Check out the other articles:

* [Reading](https://mikehuls.medium.com/image-analysis-for-beginners-how-to-read-images-video-webcam-and-screen-3778e26760e2) images, video's, your screen and the webcam
* [Detecting](https://mikehuls.medium.com/image-analysis-for-beginners-detect-and-blur-faces-with-a-simple-function-60ba60753487) and blurring faces
* [Destroying](https://mikehuls.medium.com/image-analysis-for-beginners-destroying-duck-hunt-with-opencv-e19a27fd8b6) Duck Hunt with template matching: finding images in images
* Creating a motion-detector (📍 You are here!)
* Detecting shapes without AI (under construction; coming soon)
* Detecting and reading text from images (under construction; coming soon)

## Setup

Our client asked us to create some software for analyzing transportation in a city. They want to know how many bikes, cars, buses and pedestrians visit a particular location on a given day. We've installed a webcam that films the locations.

The data-science team has some very fancy models for determining whether a particular image is a bike, bus, car of person but they cannot run this model on the entire image. It is our task to pre-process the image. We need to take small snippets that we can run the identification model on.

How do we actually detect movement? We are going to compare each frame of a video stream from my webcam to the previous one and detect all spots that have changed. The end result will look something like this:

![Our end result](https://miro.medium.com/v2/resize:fit:1216/1*pUIdN6sKkTYJlR-RO2MhlQ.gif)

Now the data science team can run their models on each green rectangle instead of the whole screen. Much smaller, and therefore, much quicker. Let's code!

## Dependencies

Instead of reading an actual webcam, we'll put a live webcam of my [beautiful](https://www.youtube.com/live/-ya9gszERU0?feature=share) city of Groningen (Netherlands) from YouTube on our screen and record that. If you want to use another source then check out [this article](https://mikehuls.medium.com/image-analysis-for-beginners-how-to-read-images-video-webcam-and-screen-3778e26760e2) to learn how to read it.

In our case we'll need the following imports:

```sh
pip install opencv-python pillow
```

## Creating the motion detector

Let's code a motion detector! We'll go through it in parts. The whole code will be available below.

## Step 1. Reading and preparing our frame

First, we'll actually read the image and convert it from OpenCV's default BGR to RGB:

```py
import cv2
import numpy as np

def motion_detector():
    frame_count = 0
    previous_frame = None

    while True:
        frame_count += 1

        # 1. Load image; convert to RGB
        img_brg = np.array(ImageGrab.grab())
        img_rgb = cv2.cvtColor(src=img_brg, code=cv2.COLOR_BGR2RGB)

        if (frame_count % 2) == 0:
            # 2. Prepare image; grayscale and blur
            prepared_frame = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            prepared_frame = cv2.GaussianBlur(src=prepared_frame, ksize=(5, 5), sigmaX=0)
```

If you've read the previous article this is nothing new; we load our image, convert its color to RGB (so that we can show it later on).

The next bit is more interesting though; we convert the image to gray and smooth it out a bit by blurring the image. Converting to grey converts all RGB pixels to a value between 0 and 255 where 0 is black and 255 is white. This is much faster than handling three values (R, G and B). This is the result:

![our original images along with our processed images](https://miro.medium.com/v2/resize:fit:1400/1*Nkkly5ZfOyGOZessg1Z2fA.gif)

## Step 2. Determine motion (change compared to the previous frame)

In this part, we'll do the actual motion detection. We'll compare the previous frame with the current one by examining the pixel values. Remember that since we've converted the image to grey all pixels are represented by a single value between 0 and 255.

In the code below we set a previous frame if there is none. Then we calculate this difference with the absdiff method. After that, we update our previous frame. Next, we dilute the image a bit. Dilation fills holes and connects areas; it makes small differences a bit clearer by increasing the size and brightness.

```py
# 3. Set previous frame and continue if there is None
if previous_frame is None:
    # First frame; there is no previous one yet
    previous_frame = prepared_frame
    continue
  
# calculate difference and update previous frame
diff_frame = cv2.absdiff(src1=previous_frame, src2=prepared_frame)
previous_frame = prepared_frame

# 4. Dilute the image a bit to make differences more seeable; more suitable for contour detection
kernel = np.ones((5, 5))
diff_frame = cv2.dilate(diff_frame, kernel, 1)

# 5. Only take different areas that are different enough (>20 / 255)
thresh_frame = cv2.threshold(src=diff_frame, thresh=20, maxval=255, type=cv2.THRESH_BINARY)[1]

```

We are not interested in pixels that are slightly brighter or darker; we use the cv2.threshold function to convert each pixel to either 0 (white) or 1 (black). The threshold for this is 20; if the difference in shades between the current and previous frame is larger than 20 we make that pixel white, else we turn it black. This is what that looks like:

![Keeping track of changing pixels](https://miro.medium.com/v2/resize:fit:1400/1*p3HwECKVZpEGQKOsexOahQ.gif)

Notice that the white dots are quite a bit bigger than the actual objects moving. This is the result of diluting the image. The bigger areas will help us when defining contours in the next part.

## Step 4. Finding areas and contouring

We want to find the area that has changed since the last frame, not each pixel. In order to do so, we first need to find an area. This is what cv.findContours does; it retrieves contours or outer limits from each white spot from the part above. In the code below we find and draw all contours.

```py
contours, _ = cv2.findContours(image=thresh_frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image=img_rgb, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
```

Two lines! Not bad. Check out the result below. Notice that we're even tracking birds!

![Drawing our contours on moving objects](https://miro.medium.com/v2/resize:fit:1216/1*ncVWucGfydMSVPbp9zF-NA.gif)

Although this looks very pretty we promised our data science team images so let's find the coordinates of the areas and call it a day:

```py
contours, _ = cv2.findContours(image=thresh_frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    if cv2.contourArea(contour) < 50:
      # too small: skip!
      continue
    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.rectangle(img=img_rgb, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2)
```


This will, again, find our contours. Then we'll loop through, discard any too small areas and retrieve the coordinates from the areas. These are the coordinates that we have to send to our data science team. For now, we'll just put a green rectangle around it with cv2.boundingRect.

## Step 5. The final step
In the previous step we've drawn the images on the RGB frame so in this very last step we just show the result:

```py
cv2.imshow('Motion detector', img_rgb)

if cv2.waitKey(30) == 27:
    break
```

In the gif below you see the end result of our analysis. Check out [this](https://www.youtube.com/watch?v=q2Urd1GNGMM) and [this](https://www.youtube.com/watch?v=jSIuji70_uk) video on YouTube for additional demonstrations. All code is available [here](https://gist.github.com/mike-huls/372d968aa523484b8cca05844dfc8443).

![The final result](https://miro.medium.com/v2/resize:fit:1216/1*pUIdN6sKkTYJlR-RO2MhlQ.gif)

Below is a quick side-by-side where we compare our input-frame, processed frame and our output. Very pretty indeed!

![All steps side by side](https://miro.medium.com/v2/resize:fit:1400/1*YGYStg7aaXl5Hsi3MGxGeg.gif)

## Conclusion

In this part of the OpenCV series, we've examined how motion detectors work. Along the way we worked with image processing; blurring, diluting, finding differences between frames. In addition, we performed some very handy analyses; finding contours and bounding boxes. Lastly, we learned about drawing rectangles and contours on the image.
