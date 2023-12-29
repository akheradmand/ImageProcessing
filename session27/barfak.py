import cv2
import numpy as np

tv_img = cv2.imread("assets/tv.png")
tv_img = cv2.cvtColor(tv_img, cv2.COLOR_BGR2GRAY)
print(tv_img.shape)

# Calculate the coordinates of the corners of the page
# tv_img[45,50] = 0
# tv_img[330,50] = 0
# tv_img[45,445] = 0
# tv_img[330,445] = 0


rows, cols=tv_img.shape
writer = cv2.VideoWriter('outputs/barfak.mp4',
                         cv2.VideoWriter_fourcc(*'mpv4'),
                         30, (cols, rows))

while True:
    my_image = np.random.random((285,395)) * 255
    my_image = np.array(my_image, dtype = np.uint8)
    tv_img[45:330,50:445] = my_image

    writer.write(tv_img)

    cv2.imshow("TV",tv_img)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

writer.release()