import cv2 as cv
from pytesseract import pytesseract
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
path_to_image = r'D:\Neeraj\python\image\abc.PNG'
pytesseract.tesseract_cmd = path_to_tesseract
img = cv.imread(path_to_image,cv.COLOR_BGR2GRAY)
imgH ,imgW,_ = img.shape
x1,y1,w1,h1 = 0,0,imgH ,imgW
text = pytesseract.image_to_string(img)
imgboxes = pytesseract.image_to_boxes(img)
imgboxes = imgboxes.splitlines()
boxes = imgboxes.split(' ')
x,y,w,h = int(imgboxes[1]),int(imgboxes[2]),int(imgboxes[3]),int(imgboxes[4])
cv.rectangle(img,(x,imgH-y),(w,imgH-h),(0,0,255),3)

# for boxes in imgboxes.splitlines():
#         boxes = boxes.split(' ')
#         x,y,w,h = int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
#         cv.rectangle(img,(x,imgH-y),(w,imgH-h),(0,0,255),3)
        # if(text == "path"):
            # x,y,w,h = int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
            # cv.rectangle(img,(x,imgH-y),(w,imgH-h),(0,0,255),3)
        # print(text)

# print(text)
cv.imshow("image",img)
# cv.imshow("box",b?ox)
cv.waitKey(0)
cv.destroyAllWindows()