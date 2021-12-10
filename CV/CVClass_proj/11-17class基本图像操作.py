from cv2 import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Turnip\Desktop\07.png')
img02 = cv2.imread(r'C:\Users\Turnip\Desktop\05.png')





# new_img = np.zeros(img.shape, np.uint8)
# cv2.circle(new_img, (150, 150), 120, (255, 255, 255), -1)
# cv2.imshow('new_img', new_img)

# and_img = cv2.bitwise_and(img, new_img)#神奇
# or_img = cv2.bitwise_or(img, new_img)#神奇
# cv2.imshow('and_img', and_img)
# cv2.imshow('or_img', or_img)

# # cv2.resize(img02, img.shape[:2])#调整img02的大小
# cv2.resize(img02, dsize=None, fx=1.5, fy=2)
#
#
# img4 = cv2.add(img, img02)#openCV相加如果超出255则取顶
# cv2.imshow('img4', img4)
#
#
# print(img02.shape)
# img03 = img + img02#需要调节大小才能合并     numpy里相加如果超出255则取余
# cv2.imshow('taotao', img02)
#
#
# img[100:400, 300:400, :] = [255, 255, 0]#往图上加个框
# # img[100:400, 300:400, :] = 100#这么写不规范
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# b, g, r = cv2.split(img)
# cv2.imshow('未拆分的原始图像', img)
# cv2.imshow('he', img03)
# cv2.imshow('blue', b)
# cv2.imshow('green', g)
# cv2.imshow('red', r)
# cv2.imshow('hsv', hsv)

# img_merge = cv2.merge([r, g, b])
# print(img.shape)
# cv2.imshow('RGB', img_merge)



cv2.waitKey()
cv2.destroyAllWindows()
