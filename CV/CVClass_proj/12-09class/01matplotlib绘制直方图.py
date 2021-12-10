from cv2 import cv2
import matplotlib.pyplot as plt

img = cv2.imread('gate.jpg')
cv2.imshow('gate', img)
# 直方图
plt.hist(img.ravel(), bins=64)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()