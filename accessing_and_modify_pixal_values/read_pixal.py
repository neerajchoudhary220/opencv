import cv2 as cv
import numpy as np
path = r'D:\Neeraj\python\image\baby.png'
img = cv.imread(path)
img_shape = img.shape
print(img_shape)
# img.item(200,200,0)
nech = img[280:340, 330:390]
img[273:333, 100:160] = nech
# px = img[200,200]
# print(px)
cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()