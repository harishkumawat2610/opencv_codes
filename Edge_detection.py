import cv2


img = cv2.imread("harish.jpg",0)
image = cv2.resize(img,(600,600))
sobel_x = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)
sobel_y = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)
sobel_or = cv2.bitwise_or(sobel_x,sobel_y)
laplacian = cv2.Laplacian(image,cv2.CV_64F)
canny = cv2.Canny(image,20,170)
cv2.imshow("Origanl image",image)
cv2.imshow("Sobel_X",sobel_x)
cv2.imshow("Sobel_Y",sobel_y)
cv2.imshow("Sobel",sobel_or)
cv2.imshow("laplacian",laplacian)
cv2.imshow("canny",canny)

cv2.waitKey(0)
cv2.destroyAllWindows()