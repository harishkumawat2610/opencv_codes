import cv2

img = cv2.imread("harish.jpg",0)
image = cv2.resize(img,(600,600))
ret ,bw =cv2.threshold(image,120,255,cv2.THRESH_BINARY)
cv2.imshow("Output",image)
cv2.imshow("BW",bw)
cv2.waitKey(0)
cv2.destroyAllWindows()