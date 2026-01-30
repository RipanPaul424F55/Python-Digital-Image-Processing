import cv2
path=r'D:\ijbgieo\photos\Album 4\20220831_232401.jpg'
image=cv2.imread(path)
window_name='image'
cv2.imshow(window_name,image)
cv2.waitKey(0)
cv2.destroyAllWindows()
