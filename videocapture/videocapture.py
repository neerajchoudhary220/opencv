from pickle import TRUE
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while TRUE:
    _,frame = cap.read()
    # hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    green = np.uint8([[[0,255,0 ]]])
    hsv = cv.cvtColor(green,cv.COLOR_BGR2HSV)
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    res = cv.bitwise_and(frame,frame, mask= mask)

    cv.imshow('frame',frame)
    # cv.imshow('mask',mask)
    cv.imshow('res',res)
    print(hsv)
    k = cv.waitKey(5) & 0xff
    if k == 27:
        break
cv.destroyAllWindows()
