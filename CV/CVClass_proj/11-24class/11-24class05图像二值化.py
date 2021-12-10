# 非黑即白，不是灰度图
from cv2 import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Turnip\Desktop\07.png')
# 先转化为灰度图，再来处理
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('img', gray)
# 然后二值化
# 第一个返回值是表示是否成功的状态值
ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)  # 参（对象， 阈值， 最大值， 类型）
cv2.imshow('binary', dst)
# cv2.imwrite('C:\\Users\Turnip\Desktop\\blackWhite.png', dst)


cv2.waitKey()
cv2.destroyAllWindows()