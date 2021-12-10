from cv2 import cv2
import numpy as np

ht = cv2.imread(r'C:\Users\Turnip\Desktop\05.png')

M = np.float32([[1, 0, -100], [0, 1, 120]])  # 平移矩阵, 两个小数组里的成员3是平移举例，可以为复制
after_pingyi = cv2.warpAffine(ht, M, (400, 400))  # c3:图像大小

cv2.imshow('after_pingyi', after_pingyi)

cv2.waitKey()
cv2.destroyAllWindows()