# 在01的基础上翻转
from cv2 import cv2

img = cv2.imread(r'C:\Users\Turnip\Desktop\2021-12-02-Pictures\background.jpg')  # 大图
templ = cv2.imread(r'C:\Users\Turnip\Desktop\2021-12-02-Pictures\template.png')  # 匹配对象
# templ = cv2.flip(templ, 0)  # 沿x轴翻转
# templ = cv2.flip(templ, -1)  # 沿y轴翻转
# templ = cv2.rotate(templ, cv2.ROTATE_180)  # 这个函数只能旋转90或者180    这里只有旋转180结果才会好
# templ = cv2.resize(templ, (121, 110))  # 尺寸变换
templ = cv2.resize(templ, None, fx=1.2, fy=1.1)  # 大小倍数变换
width, height = templ.shape[:2]
results = cv2.matchTemplate(img, templ, cv2.TM_SQDIFF_NORMED)  # 匹配 (返回的是个全是小数的矩阵)
# print(results)
minValue, maxValue, minLoc, maxLoc = cv2.minMaxLoc(results)  # 返回（最小值，最大值，最小值的坐标， 最大值的坐标）
print(minValue, maxValue, minLoc, maxLoc)  # 0.00010066070535685867 0.2145768105983734 (331, 379) (23, 163)
resultPoints1 = minLoc
resultPoints2 = (resultPoints1[0] + width, resultPoints1[1] + height)  # 右下点的横坐标
cv2.rectangle(img, resultPoints1, resultPoints2, (0, 0, 255), 2)  # 这么之后，原图中被匹配的目标就框起来了
cv2.imshow('after', img)

cv2.waitKey()
cv2.destroyAllWindows()