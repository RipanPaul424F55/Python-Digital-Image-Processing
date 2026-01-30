import cv2
import numpy as np
import matplotlib.pyplot as p
img=cv2.imread("intel.jpg")
p.imshow(img)
p.waitforbuttonpress()
p.close('all')
