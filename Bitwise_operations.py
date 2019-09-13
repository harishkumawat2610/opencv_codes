import cv2
import numpy as np

squre = np.zeros((300,300),np.uint8)
cv2.rectangle(squre,(50,50),(250,250),255,-1)
cv2.imshow("Output",squre)
cv2.waitKey(0)

ellipse = np.zeros((300,300), np.uint8)
cv2.ellipse(ellipse,(150,150),(150,150),30,0,180,255,-1)
cv2.imshow("ellipse",ellipse)
cv2.waitKey(0)
And=cv2.bitwise_and(squre,ellipse)
cv2.imshow("ANd",And)
cv2.waitKey(0)

OR=cv2.bitwise_or(squre,ellipse)
cv2.imshow("OR",OR)
cv2.waitKey(0)

NOT=cv2.bitwise_not(squre,ellipse)
cv2.imshow("Not",NOT)
cv2.waitKey(0)

XOR=cv2.bitwise_xor(squre,ellipse)
cv2.imshow("XOR",XOR)
cv2.waitKey(0)
cv2.destroyAllWindows()