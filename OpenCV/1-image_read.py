import numpy as np
import cv2


img = cv2.imread('img.jpg')
cv2.imshow('Original',img)
cv2.waitKey(0)                                      # else img will open and close at the same time
cv2.destroyAllWindows()                             # destroy all the windows opened previously
