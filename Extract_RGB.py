import cv2
import numpy as np

img = cv2.imread("harish.jpg")
image = cv2.resize(img,(600,600))
B ,G ,R = cv2.split(image)
zeros =np.zeros(image.shape[:2],dtype="uint8")
cv2.imshow("RED",cv2.merge([zeros,zeros,R]))
cv2.imshow("GEEN",cv2.merge([zeros,G,zeros]))
cv2.imshow("BLUE",cv2.merge([B,zeros,zeros]))
cv2.imshow("OUtput",image)
cv2.waitKey(0)
cv2.destroyAllWindows()