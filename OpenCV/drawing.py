# 1 - define the dimension of the image
# 2 - create the image withnumpy arrays
# 3 - create black background by filling the array with zeros
# 4 - implement drawing functions

import numpy as np
import cv2

pic = np.zeros((500,500,3),dtype='uint8') # 500 X 500 X 3 image

cv2.imshow('dark',pic)

cv2.waitKey(0)
cv2.destroyAllWindows()
