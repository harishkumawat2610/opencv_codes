import cv2
img = cv2.imread("harish.jpg")
image = cv2.resize(img,(600,600))

cv2.imshow("Output",image)
cv2.imwrite("kuma.png",image)

cv2.waitKey(0)
cv2.destroyAllWindows()