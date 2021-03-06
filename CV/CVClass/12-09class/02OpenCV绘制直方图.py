from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('gate.jpg')
histb = cv2.calcHist([img], [0], None, [256], [0, 255])
histg = cv2.calcHist([img], [1], None, [256], [0, 255])
histr = cv2.calcHist([img], [2], None, [256], [0, 255])
plt.plot(histb, color='b', label='blue-hist')
plt.plot(histg, color='g', label='green-hist')
plt.plot(histr, color='r', label='red-hist')
plt.legend(loc='upper right')  # 标记放在右上角
plt.show()


cv2.imshow('gate', img)
cv2.waitKey()
cv2.destroyAllWindows()