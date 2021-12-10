import cv2
import numpy as np

#定义回调函数
def draw_circle(event, x, y, flags, param):   #(事件名称, 坐标, 后两个参数暂时用不到但是不能省)
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 60, (0, 0, 255), -1)

img = np.zeros((500, 500, 3), np.uint8)


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):   #cv2.waitKey(1) & 0xFF只取后8位
    # if cv2.waitKey(1) == ord('q'):        #虽然这一行在我这里运行也没问题，但有的操作系统返回的不只8位
        break
    # if 0xFF == ord('q'):   #这么搞python会未响应
    #     break



# cv2.imshow('windowName', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.setMouseCallback()