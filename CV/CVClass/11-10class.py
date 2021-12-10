import cv2
import numpy as np


# img = cv2.imread(r'C:\Users\Turnip\Desktop\01.png')#导入;加上后面的参数0就变成黑白了
# img = cv2.imread(r'C:\Users\Turnip\Desktop\2k壁纸\202111215814.png')#OpenCv不支持中文路径
img = np.zeros((500,500, 3), dtype=np.uint8)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.line(img, (50, 50), (300, 355), (255, 255, 0), 10)
cv2.circle(img, (250, 250), 90, (0, 0, 255), -1)      #参数: (对象， 圆心, 半径, 颜色， 宽度)
cv2.rectangle(img, (100, 400), (100, 488), (255, 0, 0), 3)
cv2.ellipse(img, (300, 400), (150, 100), -30, 0, 360, (0, 255, 255), -1)
cv2.putText(img, 'deep Learing', (20, 360), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255))#(对象, 要写的字, 坐标, 字体)

cv2.imshow('image', img)
print(img.shape)

# cv2.imshow('winname', img)#显示#第一个参数：窗口名；第二个参数：要打开的目标
cv2.waitKey(0)         #停留（单位毫秒）
cv2.destroyAllWindows()#销毁资源，避免占用