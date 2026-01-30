import cv2
from matplotlib import pyplot as plt
x=cv2.imread("L.jpg",0)
cv2.imshow("input image",x)
hist=cv2.calcHist([x],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()
plt.waitKey(0)
