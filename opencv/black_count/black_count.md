# wtfisgoingon

https://stackoverflow.com/questions/19098104/python-opencv2-cv2-wrapper-to-get-image-size

```python
def cv_size(img):
    return tuple(img.shape[1::-1])
```

https://www.geeksforgeeks.org/python-opencv-cv2-cvtcolor-method/

```python
cv2.cvtColor(rgbImage, cv2.CV_RGB2GRAY)
```

https://chadrick-kwag.net/cv2-resize-interpolation-methods/

https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/

https://numpy.org/doc/stable/reference/generated/numpy.ndarray.size.html

```python
resizedImage = cv2.resize(grayImage, np.size(cols / 3, rows / 4), 0, 0, interpolation=cv2.INTER_LINEAR)
```

### Gray Image

```python
cv2.imwrite("Gray_Image.jpg", resizedImage)
bwImage = cv2.imread("Gray_Image.jpg")
```

### Binary Image

```python
cv2.imwrite("Binary_Image.jpg", bwImage)
cv2.imshow("Original", rgbImage)
cv2.imshow("Resized", resizedImage)
cv2.imshow("Resized Binary", bwImage)
```

### Converting an OpenCV Image to Black and White

https://stackoverflow.com/questions/7624765/converting-an-opencv-image-to-black-and-white

```python
cv2.threshold(bwImage, bwImage, 120, 255, cv2.CV_THRESH_BINARY)
```

### Display the window infinitely until any keypress

```python
cv2.waitKey(0)
```
