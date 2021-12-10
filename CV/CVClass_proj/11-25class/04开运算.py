# 开运算就是先腐蚀再膨胀
from cv2 import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Turnip\Desktop\2021-11-25-images\opening.bmp')
cv2.imshow('img', img)
kernel = np.ones((9, 9), np.uint8)
after = cv2.morphologyEx(img, cv2.MORPH_OPEN,kernel)
cv2.imshow('after', after)


cv2.waitKey()
cv2.destroyAllWindows()
