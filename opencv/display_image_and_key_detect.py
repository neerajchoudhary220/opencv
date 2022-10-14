import cv2
path =r'./image/a.png'
img = cv2.imread(path,0)
cv2.imshow("image",img)
mykey = cv2.waitKey(0)
print(mykey)
if mykey == 27: 
    cv2.destroyAllWindows()