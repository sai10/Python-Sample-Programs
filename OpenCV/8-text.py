import numpy as np
import cv2

pic = np.zeros((500,500,3),dtype='uint8')

font = cv2.FONT_HERSHEY_PLAIN
cv2.putText(pic,'Hello World',(100,100),font,3,(255,0,0),4,cv2.LINE_4)

cv2.imshow('dark',pic)

cv2.waitKey(0)
cv2.destroyAllWindows()
