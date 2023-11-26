import cv2
import numpy as np

n = 800
blank_image = np.zeros((n,n))
# cv2.imshow("",blank_image)
# cv2.waitKey()

for i in range(0,n):
    for j in range(0,n):
        if (i // 100 + j // 100) % 2 == 0:
            blank_image[i,j]=255
        else:
            blank_image[i,j]=0

cv2.imshow("",blank_image)
cv2.waitKey()
# print(blank_image)
cv2.imwrite("outputs/chess.jpg",blank_image)