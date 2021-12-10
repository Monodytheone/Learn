# 没成功，看老师！

from cv2 import cv2
import numpy as np

capture = cv2.VideoCapture(0)  # 从摄像头读取
# capture = cv2.VideoCapture(r'C:\Users\Turnip\Desktop\01.avi')  # 从文件读入
four_cc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')  # 获取OpenCV支持的视频格式
out = cv2.VideoWriter(r'C:\Users\Turnip\Desktop\out01.avi', four_cc, 20, (640, 480))  # 存到文件中
# 参数：（路径， 格式，帧率，窗口大小）

while capture.isOpened():
    ret, frame = capture.read()
    if ret:  # 如果读取成功
        out.write(frame)
        print(ret)
        cv2.imshow('img', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
capture.release()  # 释放
out.release()
