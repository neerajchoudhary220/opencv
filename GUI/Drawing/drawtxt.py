import cv2 as cv
img = cv.imread('my.png')
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'Jai Mata DI',(80,50), font, 1,(200,0,200),4,cv.MARKER_DIAMOND)
cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()