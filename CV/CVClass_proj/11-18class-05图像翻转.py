from cv2 import cv2
import numpy as np

ht = cv2.imread(r'C:\Users\Turnip\Desktop\05.png')

dst = cv2.flip(ht, 0)  # 沿x轴翻转
dst2 = cv2.flip(ht, 1)  # 沿y轴翻转
dst3 = cv2.flip(ht, -1)  # x, y轴都翻转


cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.waitKey()
cv2.destroyAllWindows()