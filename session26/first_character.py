import cv2
import numpy as np

blank_image = np.zeros((500,420))

# blank_image[400:450,100:120]=255
blank_image[350:400,100:120]=255
blank_image[300:350,120:140]=255
blank_image[250:300,140:160]=255
blank_image[200:250,160:180]=255
blank_image[150:200,180:200]=255
blank_image[100:150,200:220]=255

blank_image[150:200,220:240]=255
blank_image[200:250,240:260]=255
blank_image[250:300,260:280]=255
blank_image[300:350,280:300]=255
blank_image[350:400,300:320]=255

blank_image[230:250,180:240]=255

cv2.imwrite("outputs/A_character.jpg", blank_image)