import cv2
import numpy as np

img = cv2.imread("harish.jpg")
image = cv2.resize(img,(600,600))
blue = cv2.blur(image,(3,3))
Gauss= cv2.GaussianBlur(image,(7,7),0)
median = cv2.medianBlur(image,5)
Bil = cv2.bilateralFilter(image,9,75,75)
cv2.imshow("Origanl image",image)
cv2.imshow("blur",blue)
cv2.imshow("GaussianBlur",Gauss)
cv2.imshow("Median",median)
cv2.imshow("Bil",Bil)
cv2.waitKey(0)
cv2.destroyAllWindows()