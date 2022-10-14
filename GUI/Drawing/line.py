import cv2 as cv
img = cv.imread('my.png')
cv.line(img,(2,2),(510,510),(255,0,0),2)
#cv.line(img,(x,y),(x1,y1),(color code),line_size)
cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()