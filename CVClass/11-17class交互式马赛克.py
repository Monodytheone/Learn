from cv2 import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Turnip\Desktop\05.png')

enable = False  # 表示鼠标是否点下


# 定义回调函数
def call_back_draw(event, x, y, flags, param):
    global enable  # 设为全局变量
    if event == cv2.EVENT_LBUTTONDOWN:
        enable = True
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if enable:
            drawMask(y, x)  # 调用马赛克函数
            # drawMask(x, y)  # 调用马赛克函数 这么不行
        elif event == cv2.EVENT_LBUTTONUP:
            enable = False


def drawMask(x, y, size=20):
    a = 20
    # m = np.uint8(x / size) * size  # m和n应该是马赛克方块的左上点坐标, 马赛克方块的长度宽度为size
    # n = np.uint8(y / size) * size

    # m = np.uint8(x / a) * a  # 改变这个a的大小会影响马赛克方块的密度, 为1,100等特殊值时还会出现同时画多个块的奇怪现象
    # n = np.uint8(y / a) * a

    m = (int)(x / a) * a
    n = (int)(y / a) * a

    # m = np.uint8(x)
    # n = np.uint8(y)

    # size大小范围内的图像像素值设置为同一个像素值
    for i in range(size):
        for j in range(size):
            img[m + i][n + j] = img[m][n]  # 这里没有用第三维，上一个自动马赛克是否也可以不用第三维呢？


cv2.namedWindow('image')
cv2.setMouseCallback('image', call_back_draw)

while 1:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 退出条件
        break
