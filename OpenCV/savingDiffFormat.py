import cv2

img = cv2.imread('img.jpg')

img = cv2.imwrite('image.png',img)

cv2.imshow('Original',img)

cv2.waitKey(0)

cv2.destroyAllWindows()
