import cv2
import numpy as np

img = cv2.imread("harish.jpg")
image = cv2.resize(img,(600,600))
kernel_3x3 = np.ones((7,7),np.float32)/49
blurred = cv2.filter2D(image,-1,kernel_3x3)
cv2.imshow("Origanl image",image)
cv2.imshow("Rotation Image",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()