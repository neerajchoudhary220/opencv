import cv2
img = cv2.imread('a.png')
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# h,w = img.shape[:2]

# # print("Height is {} and width is {}".format(h,w))
# (B,G,R) = img[100,100]
# print("R={}, G={}, B={}".format(R,G,B))
# G=img[100,100,1]
# print("G=",G)

