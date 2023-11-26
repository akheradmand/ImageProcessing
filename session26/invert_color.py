import cv2

image_name = input("please enter full name of image: ")
image = cv2.imread(f"assets/{image_name}")
# cv2.imshow("",image)
# cv2.waitKey()

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        image[i,j] = 255 - image[i,j]

invert_image = cv2.imwrite(f"outputs/invert_{image_name}" , image)