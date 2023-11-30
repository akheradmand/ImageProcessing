import cv2
import time

image = cv2.imread("wolf.jpg")
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

print(image.shape)

rows , cols = image.shape

threshold = 120

start_time = time.time()
# option 1
# for r in range(rows):
#     for c in range(cols):
#         if image[r, c] > threshold:
#             image[r, c] = 255
#         else:
#             image[r, c] = 0

# option 2
# image[image > threshold] = 255
# image[image <= threshold] = 0

# option 3
_ , image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)  # less time

end_time = time.time()
print(end_time - start_time)

cv2.imshow("threshold image", image)
cv2.waitKey()