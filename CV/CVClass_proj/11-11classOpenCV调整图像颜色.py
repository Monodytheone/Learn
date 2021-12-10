import cv2
import numpy as np
import sys

# cv2.createTrackbar()
# cv2.getTrackbarPos()

def call_back_bringtness(param):   #此参数用不到但不能没有
    global value, img, img1
    value =  cv2.getTrackbarPos('brightness', 'Brighter')
    img1 = np.uint8(np.clip((value/100 * img), 10, 255))

img = cv2.imread(r'C:\Users\Turnip\Desktop\02.png')
img1 = img.copy()

if img is None:
    print('Falied to read the 02.png')
    sys.exit()

cv2.namedWindow('Brighter', cv2.WINDOW_NORMAL)
value = 80
cv2.createTrackbar('brightness', 'Brighter', value, 255, call_back_bringtness)   #参数3：当前值；参数4：滑动块最大值
while True:
    cv2.imshow('Brighter', img1)
    if cv2.waitKey(1)&0xFF == 27:   #Esc键的ASCII码是27
        break
cv2.destroyAllWindows()