import cv2 as cv
flags = [i for i in dir(cv) if i.startswith('COLOR_')]
f= open('flag.txt','w',encoding='utf8')
f.write(str(flags)+"\n")