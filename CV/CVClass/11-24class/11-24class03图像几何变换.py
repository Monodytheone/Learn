# 首先生成一个矩阵，然后把矩阵作用在变换对象上，.就行了
from cv2 import cv2
import numpy as np


img = cv2.imread(r'C:\Users\Turnip\Desktop\07.png')
cv2.imshow('img', img)
h, w = img.shape[:2]
x_h = int(h / 2)
y_w = int(w / 2)
M = cv2.getRotationMatrix2D((x_h, y_w), 90, 0.8)  # 旋转矩阵
dst = cv2.warpAffine(img, M, (h, w))  # 仿射变换
cv2.imshow('rotate', dst)

cv2.waitKey()
cv2.destroyAllWindows()