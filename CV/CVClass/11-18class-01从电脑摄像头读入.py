from cv2 import cv2
import numpy as np

capture = cv2.VideoCapture(0)  # 从摄像头读取
while capture.isOpened():  # 当摄像头打开
    ret, frame = capture.read()  # 有两个返回值， 第一个bool代表摄像头采集是否成功, 第二是就是采集到的东西
    print(ret)
    cv2.imshow('img', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
capture.release()  # 释放
