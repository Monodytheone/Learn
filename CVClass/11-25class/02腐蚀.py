from cv2 import cv2
import numpy as np


# img = cv2.imread(r'C:\Users\Turnip\Desktop\2021-11-25-images\tophat2.bmp')
# cv2.imshow('img', img)
# kernel = np.ones((5, 5), np.uint8)
# erode_img = cv2.erode(img, kernel)
# cv2.imshow('erode_img', erode_img)

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 75))
img2 = np.zeros((600, 600), np.uint8)
cv2.circle(img2, (300, 300), 120, (255, 255, 255), -1)
erode2 = cv2.erode(img2, kernel)
cv2.imshow('img2', img2)
cv2.imshow('erode2', erode2)


cv2.waitKey()
cv2.destroyAllWindows()
