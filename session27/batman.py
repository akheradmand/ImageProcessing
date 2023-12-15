import cv2

image = cv2.imread("assets/bat.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_ , image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY_INV)
cv2.putText(image,"BATMAN", (380,500),cv2.FONT_HERSHEY_SIMPLEX, 2, 255)

cv2.imshow("result", image)
cv2.waitKey()

cv2.imwrite("outputs/batman.jpg", image)