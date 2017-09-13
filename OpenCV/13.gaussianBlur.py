import cv2

pic = cv2.imread('img.jpg')

matrix = (7,7)

blur = cv2.GaussianBlur(pic,matrix,0) # sigmax = std dev. on x-axis and sigmay = std dev. on y-axis

cv2.imshow('blurred',blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
