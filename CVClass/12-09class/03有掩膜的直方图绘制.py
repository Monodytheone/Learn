from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('gate.jpg')
h, w, c = img.shape
mask = np.zeros((h, w), np.uint8)  # 掩膜图片
h1 = np.int0(h / 4)
h2 = np.int0(h * 0.75)
w1 = np.int0(h / 4)
w2 = np.int0(w * 0.75)

# histb = cv2.calcHist([img], [0], None, [256], [0, 255])
# histg = cv2.calcHist([img], [1], None, [256], [0, 255])
# histr = cv2.calcHist([img], [2], None, [256], [0, 255])
# plt.plot(histb, color='b', label='blue-hist')
# plt.plot(histg, color='g', label='green-hist')
# plt.plot(histr, color='r', label='red-hist')
# plt.legend(loc='upper right')  # 标记放在右上角
# plt.show()


cv2.imshow('mask', mask)
# cv2.imshow('gate', img)
cv2.waitKey()
cv2.destroyAllWindows()
