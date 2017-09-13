import numpy as np
import cv2

pic = np.zeros((500,500,3),dtype='uint8')

font = cv2.FONT_HERSHEY_PLAIN
cv2.rectangle(pic,(100,0),(400,150),(223,200,98),13,lineType=8,shift=0)
cv2.line(pic,(350,350),(500,350),(0,0,255))
cv2.circle(pic,(250,250),50,(0,0,155))
cv2.putText(pic,'Hello World',(100,100),font,3,(255,0,0),4,cv2.LINE_4)

cv2.imshow('dark',pic)

cv2.waitKey(0)
cv2.destroyWindow()
