# 闭运算就是先膨胀再腐蚀
# 闭运算有助于关闭前景物体内部的小孔，或物体上的小黑点

from cv2 import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Turnip\Desktop\2021-11-25-images\closing.bmp')
cv2.imshow('img', img)
kernel = np.ones((9, 9), np.uint8)  # 卷积核
after = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow('after', after)

cv2.waitKey()
cv2.destroyAllWindows()

