import numpy as np
import cv2


#img = cv2.imread('img.jpg',0)                       # to print the image in grayscale
img = cv2.imread('img.jpg',1)                       # RGB image , even -1 will work
cv2.imshow('Original',img)                          # 'Original' is the title of the image
cv2.waitKey(0)                                      # else img will open and close at the same time
cv2.destroyAllWindows()                             # destroy all the windows opened previously
