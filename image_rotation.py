import cv2

img = cv2.imread("harish.jpg")
image = cv2.resize(img,(600,600))
height,width = image.shape[:2]
rotation_matrix =cv2.getRotationMatrix2D((height/2,width/2),90,.8)
rotation_image=cv2.warpAffine(image,rotation_matrix,(width,height))
cv2.imshow("Origanl image",image)
cv2.imshow("Rotation Image",rotation_image)
cv2.waitKey(0)
cv2.destroyAllWindows()