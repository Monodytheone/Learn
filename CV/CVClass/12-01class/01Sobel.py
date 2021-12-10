from cv2 import cv2
import numpy as np


img = cv2.imread(r'C:\Users\Turnip\Desktop\2021-12-01--image\sobel.bmp', 0)
# 进行边缘检测
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobel_y = cv2.convertScaleAbs(sobel_y)

soble_add_xy = cv2.addWeighted(sobel_y, 0.5, sobel_x, 0.5)
cv2.imshow('add', soble_add_xy)
cv2.imshow('sobel_x', sobel_x)
cv2.imshow('sobel_y', sobel_y)

sobel_plus = sobel_y + sobel_x
cv2.imshow('plus', sobel_plus)

print(img.shape)
cv2.imshow('img', img)


cv2.waitKey()
cv2.destroyAllWindows()