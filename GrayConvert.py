import cv2
import sys
x=cv2.imread("L.jpg")
gray=cv2.cvtColor(x,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original",x)
cv2.imshow("Gray",gray)
(thres,Binary)=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
cv2.imshow("Binary image",Binary)
print(sys.getsizeof(x)," bytes or %d MB"%(sys.getsizeof(x)/pow(2,20)))
cv2.waitKey(0)
cv2.destroyAllWindows()
