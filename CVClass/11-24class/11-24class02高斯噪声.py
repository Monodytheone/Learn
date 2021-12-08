from cv2 import cv2
import numpy as np


def gauss_noise(image, mean=0, var=0.001):
    image = np.array(image/255, np.float32)  # 除255之后取值就是0~1之间了,符合标准正态分布，最后再放大就行了
    noise = np.random.normal(mean, var**0.5, image.shape)  # 参2：这里要标准差，所以开根号
    out = image + noise
    if out.min() < 0:
        low_clip = 1
    else:
        low_clop = 0
