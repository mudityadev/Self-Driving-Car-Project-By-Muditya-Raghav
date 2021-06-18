import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2  #bringing in OpenCV libraries

low_threshold = 100
high_threshold = 200

image = mpimg.imread('exit-ramp.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #grayscale conversion
edges = cv2.Canny(gray, low_threshold, high_threshold)

plt.imshow(gray, cmap='gray')


plt.imshow(edges)

plt.show()