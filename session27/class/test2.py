import cv2
import numpy as np

my_image = np.ones((500,800), dtype=np.uint8) * 255

# barfak
# my_image = np.random.random((250, 350)) * 255
# my_image = np.array(my_image, dtype=np.uint8)

cv2.rectangle(my_image, (30,35), (350,410), 128, 10)
cv2.circle(my_image, (600,200), 100, 120, 4)

cv2.putText(my_image, "Python is the best programing language", (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, 100)

print(my_image)

cv2.imshow("result", my_image)
cv2.waitKey()