from cv2 import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Turnip\Desktop\2021-11-25-images\erode.bmp')
cv2.imshow('img', img)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))  # c2：卷积核大小
dilate_img = cv2.dilate(img, kernel)
cv2.imshow('dilate_img', dilate_img)

cv2.waitKey()
cv2.destroyAllWindows()
