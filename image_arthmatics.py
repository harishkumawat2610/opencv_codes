import cv2
import numpy as np

img = cv2.imread("harish.jpg")
image = cv2.resize(img,(600,600))
height,width = image.shape[:2]
m = np.ones(image.shape,dtype="uint8")*150

add = cv2.add(image,m)
sub = cv2.subtract(image,m)
mul = cv2.multiply(image,m)
cv2.imshow("Orignal iMage",image)
cv2.imshow("add",add)
cv2.imshow("sub",sub)
cv2.imshow("mul",mul)
cv2.waitKey(0)
cv2.destroyAllWindows()