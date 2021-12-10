# 黑帽图像 = 闭运算图像 - 原始图像
# 得到图像内部的小孔，或前景色中的小黑点

# 礼帽运算：保留噪声

from cv2 import cv2
import numpy as np

# img = cv2.imread(r'C:\Users\Turnip\Desktop\2021-11-25-images\blackhat.bmp')
img = cv2.imread(r'C:\Users\Turnip\Desktop\07.png')
cv2.imshow('img', img)
kernel = np.ones((9, 9), np.uint8)  # 卷积核
after = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('after', after)

cv2.waitKey()
cv2.destroyAllWindows()

