import cv2

source_image = cv2.imread("assets/minavand.jpg")
source_image_gray = cv2.cvtColor(source_image , cv2.COLOR_BGR2GRAY)

x = source_image_gray.shape[0]//4
for i in range(0,x):
    for j in range(0,x-i):
        if (i+j > x//2):
            source_image_gray[i , j] = 0

cv2.imwrite("outputs/death_symbol_minavand.jpg" , source_image_gray)