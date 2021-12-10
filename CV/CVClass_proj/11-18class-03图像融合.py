from cv2 import cv2
import numpy as np

xiaogong = cv2.imread(r'C:\Users\Turnip\Desktop\04.png')
hutao = cv2.imread(r'C:\Users\Turnip\Desktop\05.png')
print(xiaogong.shape, hutao.shape)
h, w = hutao.shape[:2]
xiaogong = cv2.resize(xiaogong, (w, h))
hebing = xiaogong + hutao  # 通过np简单融合
hebing2 = cv2.add(xiaogong, hutao)  # 通过OpenCV简单融合
hebing3 = cv2.addWeighted(xiaogong, 0.1, hutao, 1, 1)  # 2, 4号参数是权重，5号参数是亮度（可正可负）

cv2.addWeighted
print(hutao.shape, hebing.shape)
# cv2.imshow('img', xiaogong)
# cv2.imshow('hutao', hutao)
# cv2.imshow('hebing', hebing)
# cv2.imshow('hebing2', hebing2)
cv2.imshow('hebing3', hebing3)

cv2.waitKey(0)
cv2.destroyAllWindows()
