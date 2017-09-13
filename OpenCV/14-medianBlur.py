import cv2

pic  = cv2.imread('img.jpg')
kernal = 3

# mainly used for salt and pepper noise

median = cv2.medianBlur(pic,kernal)

cv2.imshow('median blur',median)

cv2.waitKey(0)
cv2.destroyAllWindows()
