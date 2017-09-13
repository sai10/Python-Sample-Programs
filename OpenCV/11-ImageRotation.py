import numpy as np
import cv2

pic = cv2.imread('img.jpg')

 rows = pic.shape[0]
cols = pic.shape[1]
center = (cols/2,rows/2)
angle = 90
M = cv2.getRotationMatrix2D(center,angle,1) # 1 is the scaling factor
rotate = cv2.warpAffine(pic,M,(cols,rows))
cv2.imshow('rotated',rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()
