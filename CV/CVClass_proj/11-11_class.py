import cv2
import numpy as np

drawing = False
mode = True
ix, iy = 1, -1


#定义回调函数
def call_back_draw(event, x, y, flags, param):
    global drawing, mode, ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True        #首先判断鼠标左键是否按下
        ix, iy = x, y
    elif event==cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)      #画矩形
            else:
                cv2.circle(img, (x, y), 3, (0,0,255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


img = np.ones((600, 600, 3), np.uint8) * 50     #乘的数不同，颜色会有不同，好像是灰度之类的概念

cv2.namedWindow('image')
cv2.setMouseCallback('image', call_back_draw)#调用回调函数的函数

while True:
    cv2.imshow('image222', img)
    if cv2.waitKey(1)&0xFF == ord('m'):
        mode = not mode
    elif cv2.waitKey(1)&0xFF == ord('q'):
        break



# cv2.imshow('pic', img)
# cv2. waitKey(0)
cv2.destroyAllWindows()