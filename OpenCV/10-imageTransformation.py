import numpy as np
import cv2

pic = cv2.imread('img.jpg')
rows = pic.shape[0]
cols = pic.shape[1]

M = np.float32([[1,0,150],[0,1,70]]) # 150 pixels to right and 70 pixels down

shifted = cv2.warpAffine(pic,M,(cols,rows))
cv2.imshow('shifted',shifted)

cv2.waitKey(0)
cv2.destroyWindow()
