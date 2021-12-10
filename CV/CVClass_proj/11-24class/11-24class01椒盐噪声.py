from cv2 import cv2
import numpy as np


# 椒盐噪声
def salt_pepper_noise(image, ratio):
    out = np.zeros(image.shape, np.uint8)
    thres = 1-ratio  # 阈值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = np.random.random()  # 0~1之间的随机数
            if rdn < ratio:
                out[i][j] = 0
            elif rdn > thres:
                out[i][j] = 255  # 白点
            else:
                out[i][j] = image[i][j]  # 不生成椒盐点
    return out


img = cv2.imread(r'C:\Users\Turnip\Desktop\07.png')  # 如果是正斜杠就不用加 r
cv2.imshow('img', img)
out_sp_noise = salt_pepper_noise(img, 0.02)
cv2.imshow('after_sp_noise', out_sp_noise)
# 椒盐噪声加好了，开始通过模糊去噪
dst = cv2.blur(out_sp_noise, (5, 5))  # 均值模糊
cv2.imshow('dst', dst)
# 高斯模糊
after_GaussianBlur = cv2.GaussianBlur(out_sp_noise, (9, 9), 2, 2)
cv2.imshow('after_GaussionBlur', after_GaussianBlur)
# 中值模糊
after_medianBlur = cv2.medianBlur(out_sp_noise, 11)
cv2.imshow('medianBlur', after_medianBlur)
cv2.waitKey()
cv2.destroyAllWindows()

