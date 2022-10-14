from PIL import Image
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
from pytesseract import pytesseract
#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

path_to_image = r'D:\Neeraj\python\image\abc.PNG'
pytesseract.tesseract_cmd = path_to_tesseract

img = cv.imread(path_to_image,cv.COLOR_BGR2GRAY)

#Extract text from image
text = pytesseract.image_to_string(img)
print(text)