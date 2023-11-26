import cv2


my_image = cv2.imread("1.jpg")  #خواندن عکس
my_image2 = cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY) #تبدیل به سیاه سفید

# print(my_image2)  #نمایش ارایه
print(my_image2.shape) #نمایش ابعاد
print(my_image2[10,15])

# my_image2[10,15]=0
# my_image2[10,16]=0
# my_image2[10,17]=0
# my_image2[11,15]=0
# my_image2[11,16]=0
# my_image2[11,17]=0

# my_image2[10:12,15:18]=0

my_image2[0:30,0:768]=0 #ضلع بالا
my_image2[0:432,0:30]=0 #ضلع چپ
my_image2[0:432,738:768]=0 #ضلع راست
my_image2[402:432,0:768]=0 #ضلع پایین

tea=my_image2[270:400,40:180] #انتخاب استکان چای
my_image2[290:420,370:510]=tea

cv2.imshow("",my_image2) #نمایش عکس جدید
cv2.waitKey()
cv2.imwrite("result.jpg",my_image2) #ذخیره عکس جدید