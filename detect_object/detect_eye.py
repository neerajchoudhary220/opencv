import cv2 as cv
path = 'men.jpg'
img = cv.imread(path)
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
c_classifier = cv.CascadeClassifier("cars.xml")
d_objects = c_classifier.detectMultiScale(gray_img, minSize=(25, 25))
# d_objects =[[221,123,33, 33],[24,273,29, 29]]
if len(d_objects) != 0:
    for (x, y, h, w) in d_objects:
       total = cv.rectangle(img, (x, y), ((x + h), (y + w)), (0, 255, 0), 3)

print(d_objects)
cv.imshow("Detected Objects",img)
cv.waitKey(0)
cv.destroyAllWindows()