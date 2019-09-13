import cv2

img = cv2.imread("harish.jpg")
cv2.imshow("Output windows",img)
print(img.shape)
print("height pixes values",img.shape[0])
print("width pixels values",img.shape[1])
print("layer pixels values",img.shape[2])
cv2.waitKey(0)
cv2.destroyAllWindows()