import cv2

img = cv2.imread("harish.jpg")
image = cv2.resize(img,(600,600))
rotation_image = cv2.transpose(image)
cv2.imshow("Origanl image",image)
cv2.imshow("Rotation Image",rotation_image)
cv2.waitKey(0)
cv2.destroyAllWindows()