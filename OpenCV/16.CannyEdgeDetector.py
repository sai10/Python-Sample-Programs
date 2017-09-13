import cv2

pic  = cv2.imread('img.jpg')

thres1 = 50
thres2 = 100

canny = cv2.Canny(pic,thres1,thres2)
cv2.imshow('canny',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()


