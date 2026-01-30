import cv2
import numpy as np
img1=cv2.imread("Figure_1.png")
img2=cv2.imread("Figure_2.png")
#weightedSum=cv2.addWeighted(img1,0.5,img2,0.4,0)
for i in range(1,10):
    for j in range(1,10):
        cv2.imshow("the weighted image",(cv2.addWeighted(img1,(i/10),img2,(j/10),0)))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
