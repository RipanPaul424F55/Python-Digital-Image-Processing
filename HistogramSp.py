import cv2
import numpy as np
from matplotlib import pyplot as plt
x=cv2.imread("L.jpg")
print(x.ravel())
cv2.imshow("Original",x)
list=x.ravel() #converts the image matrix into a linear 1D matrix
print("length ",len(list)," pixels")
#plt.hist(list,256,[0,256])
#plt.show()
print("After sorting the array")
list=list.sort()
plt.hist(list,256,[0,256])
plt.show()
