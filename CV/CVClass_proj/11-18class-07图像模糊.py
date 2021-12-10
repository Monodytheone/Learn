from cv2 import cv2
import numpy as np

ht = cv2.imread(r'C:\Users\Turnip\Desktop\05.png')


# 这个不知道叫啥模糊
after_blur = cv2.blur(ht, (11, 11))  # 进行模糊, c2两个数字越大（即盒子越大），模糊效果越明显,盒长一般取基数

# 中值模糊
after_mediamBlur = cv2.medianBlur(ht, 11)

# 高斯模糊(高斯分布就是正态分布)
after_gaussian_blur = cv2.GaussianBlur(ht, (11, 11), 5, 5)


cv2.imshow('after_blur', after_blur)
# cv2.imshow('ht', ht)
# cv2.imshow('after_mediamBlur', after_mediamBlur)
# cv2.imshow('after_gaussian_blur', after_gaussian_blur)
cv2.waitKey()
cv2.destroyAllWindows()