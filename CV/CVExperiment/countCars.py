import cv2
import numpy as np

min_w = 90
min_h = 90

# 检测线的高度
line_high = 550

# 线的偏移
offset = 7

# 统计车的数量
carno = 0

# 存放有效车辆的数组
cars = []


def center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1

    return cx, cy


cap = cv2.VideoCapture('video.mp4')

bgsubmog = cv2.createBackgroundSubtractorMOG2()
# 形态学kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

while True:
    ret, frame = cap.read()
    if (ret == True):

        # 灰度
        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 去噪（高斯）
        blur = cv2.GaussianBlur(frame, (3, 3), 5)
        # 去背影
        mask = bgsubmog.apply(blur)

        # 腐蚀， 去掉图中小斑块
        erode = cv2.erode(mask, kernel)

        # 膨胀， 还原放大
        dilate = cv2.dilate(erode, kernel, iterations=3)

        # 闭操作，去掉物体内部的小块
        close = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
        close = cv2.morphologyEx(close, cv2.MORPH_CLOSE, kernel)

        cnts, h = cv2.findContours(close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # 画一条检测线
        cv2.line(frame, (10, line_high), (1200, line_high), (255, 255, 0), 3)

        for (i, c) in enumerate(cnts):
            (x, y, w, h) = cv2.boundingRect(c)

            # 对车辆的宽高进行判断
            # 以验证是否是有效的车辆
            isValid = (w >= min_w) and (h >= min_h)
            if not isValid:
                continue
            if not 1:

