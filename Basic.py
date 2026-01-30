import cv2
def error(x,y):
    try:
        cv2.imshow("p1/p2",(x/y))
    except:
        print("error")
a=cv2.imread("p1.jpg")
b=cv2.imread("p2.jpg")
cv2.imshow("p1",a)
cv2.imshow("p2",b)
cv2.imshow("p1+p2",(a+b))
cv2.imshow("p1-p2",(a-b))
cv2.imshow("p1*p2",(a*b))
error(a,b)
cv2.waitKey(0)
cv2.destroyAllWindows()
