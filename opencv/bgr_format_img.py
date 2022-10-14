import cv2
path = r'./imge/a.png';
img = cv2.imread(path, 0)
copy_path =r'./image/copy.png'
cv2.imwrite('neeraj.png',img) #save image

# Displaying the image
# cv2.imshow('image', img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
print("copy has been successfully")



