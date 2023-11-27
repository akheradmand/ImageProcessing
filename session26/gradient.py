import cv2
import numpy as np

n = 255
blank_image = np.zeros((n+1,n+1))

for i in range(n+1):
    blank_image[i,:] = i

cv2.imwrite("outputs/gradient.jpg" , blank_image)