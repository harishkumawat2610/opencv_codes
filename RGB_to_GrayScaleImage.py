import cv2
#method 1
#img = cv2.imread("harish.jpg",0)
img = cv2.imread("harish.jpg")
image = cv2.resize(img,(600,600))

cv2.imshow("Output",image)
print("Gray Image info",image.shape)
#method 2
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image",gray)
print("Gray Image info",gray.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()