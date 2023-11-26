import cv2
import numpy as np

sad_image = cv2.imread("assets/sad_mans.jpg")
sad_image_gray = cv2.cvtColor(sad_image , cv2.COLOR_BGR2GRAY)
sad_image_shape = sad_image_gray.shape
blank_image = np.zeros((sad_image_shape[0], sad_image_shape[1]))

# print(sad_image_gray)

for i in range(sad_image_shape[0]):
    for j in range(sad_image_shape[1]):
        blank_image[i,j] = sad_image_gray[sad_image_shape[0]-1-i,sad_image_shape[1]-1-j]

cv2.imwrite("outputs/happy_mans.jpg" , blank_image)