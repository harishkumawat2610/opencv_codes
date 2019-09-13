import cv2

img = cv2.imread("harish.jpg")
image = cv2.resize(img,(600,600))
height,width = image.shape[:2]
s_row,s_col = int(height*.25),int(width*.25)
e_row,e_col = int(height*.75),int(width*.75)
cropped = img[s_row:e_row,s_col:e_col]
cv2.imshow("Orignal iMage",image)
cv2.imshow("Cropping iMage",cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()