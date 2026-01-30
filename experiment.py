import cv2
x=cv2.imread("L.jpg")
y=cv2.imread("L.jpg",0)
cv2.imshow("taken with 0",y)
cv2.imshow("using attribute",cv2.cvtColor(x,cv2.COLOR_BGR2GRAY))
 #                                           cv2.cvtColor(x,cv2.COLOR_BGR2GRAY)
print(len(x))
cv2.waitKey(0)
cv2.deatroyAllWindows()