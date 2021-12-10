from cv2 import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Turnip\Desktop\05.png')
# cv2.imshow('img', img)
# img[100:200, 100:200, :] = [200, 250, 169]


#随机颜色
img[100:200, 100:200, :] = np.random.randint(0, 255, size=(3, ))


cv2.imshow('new', img)
cv2.waitKey()
cv2.destroyAllWindows()