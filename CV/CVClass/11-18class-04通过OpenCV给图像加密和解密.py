from cv2 import cv2
import numpy as np

def encode(img_tar, img_key):  # 参数2：秘钥图像
    result = cv2.bitwise_xor(img_tar, img_key)  # 加密
    return result


ht = cv2.imread(r'C:\Users\Turnip\Desktop\05.png')
h, w, c = ht.shape

key = np.random.randint(0, 256, (h, w, c), np.uint8)  # 随机生成大小与图片相等的秘钥图像
cv2.imshow('ht', ht)
# cv2.imshow('img_key', key)

# 进行加密
after_encode = encode(ht, key)

# 进行解密
after_double_encode = encode(after_encode, key)  # 把这个输出就是加密之前的图像


cv2.imshow('after_double', after_double_encode)
cv2.imshow('after_encode', after_encode)


cv2.waitKey()
cv2.destroyAllWindows()
