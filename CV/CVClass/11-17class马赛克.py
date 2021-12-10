from cv2 import cv2
import numpy as np

# 思路：把图片横竖都分为cheng份，每一份都转为这个小方块左上点的颜色

cheng = 20

img = cv2.imread(r'C:\Users\Turnip\Desktop\05.png')
print(img)
print(img.shape)
height = img.shape[0]
width = img.shape[1]

# uint8的范围是0~255
numHeight = np.uint8(height / cheng)  # 强制转换为整数
numWidth = np.uint8(width / cheng)
new_img = np.zeros((height, width, 3), np.uint8)
# new_img = np.zeros(img.shape, np.uint8)  # 同上

for i in range(cheng):
    y = i * numHeight
    for j in range(cheng):
        x = j * numWidth

        b = img[y, x][0]  # 0通道
        g = img[y, x][1]  # 1通道
        r = img[y, x][2]  # 通道

        for n in range(numHeight):
            for m in range(numWidth):
                new_img[y+n, x+m, 0] = b
                new_img[y+n, x+m, 1] = g
                new_img[y+n, x+m, 2] = r


cv2.imshow('new_img', new_img)
cv2.waitKey()
cv2.destroyAllWindows()