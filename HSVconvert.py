import cv2
x=cv2.imread("L.jpg")
cv2.imshow("Original",x)
cv2.imshow("HSV",cv2.cvtColor(x,cv2.COLOR_BGR2HSV))
cv2.waitKey(0)
cv2.destroyAllWindows()
