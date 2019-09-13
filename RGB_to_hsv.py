import cv2

img = cv2.imread("harish.jpg")
image = cv2.resize(img,(600,600))
img_hsv =cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("Hsv",img_hsv)
cv2.imshow("Output",image)
cv2.imshow("H",img_hsv[: , : , 0])
cv2.imshow("s",img_hsv[: , : , 1])
cv2.imshow("v",img_hsv[: , : , 2])
cv2.waitKey(0)
cv2.destroyAllWindows()