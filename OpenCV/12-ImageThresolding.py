import cv2

pic = cv2.imread('img.jpg',0) # loading in greyscale

thresoldValue = 200

(T_value,binary_thresold) = cv2.threshold(pic,thresoldValue,255,cv2.THRESH_BINARY)

cv2.imshow('binary',binary_thresold)
cv2.waitKey(0)
cv2.destroyAllWindows()
