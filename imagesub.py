import cv2
import numpy as np
img1=cv2.imread("p1.jpg")
img2=cv2.imread("p2.jpg")
diff=cv2.subtract(img1,img2)
result=np.any(diff)
if result is False:
    print("Both images are same")
else:
    print("Images are different")
cv2.imshow("Difference",diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
