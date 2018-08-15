import os
import cv2 as cv
import pandas as pd

cv.namedWindow("Image",cv.WINDOW_NORMAL)

path = "/Volumes/MachsionHD/USCdata/image_label/1/900.jpg"
img = cv.imread(path)
x1=486.797872340426
y1=205.265957446809
x2=x1+316.595744680851
y2=y1+110.297872340425
cv.rectangle(img,(int(x1),int(y1)),(int(x2),int(y2)),(55,255,155),5)
cv.imshow("Image",img)
cv.waitKey(0)
cv.destroyAllWindows() 