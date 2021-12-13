# 本案例通过分水岭算法对一幅肺癌细胞图像进行分割，代码给出了较详细必要的注释


from cv2 import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def watershed_demo(img):
    print(img.shape)
    # 去噪声
    blurred = cv.pyrMeanShiftFiltering(img, 10, 100)  # 均值漂移函数
    # 灰度/二值图像
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow('thresh', thresh)
    # 有很多的黑点，所以我们去黑点噪声
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3)) 
# 构造图像形态学操作中用到的结构元素（其实就是kernel）
    opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)
    cv.imshow('opening ', opening)
    sure_bg = cv.dilate(opening, kernel, iterations=3)
    cv.imshow('mor-opt', sure_bg)
    # 距离变换
    dist = cv.distanceTransform(opening, cv.DIST_L2, 3)  
# 距离变换函数，该函数用于计算图像中每一个非零点像素与其最近的零点像素之间的距离，输出的是保存每一个非零点与最近#零点的距离信息；
    dist_output = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)
    cv.imshow('distance-t', dist_output * 50)
    ret, surface = cv.threshold(dist, dist.max()*0.6, 255, cv.THRESH_BINARY)
    cv.imshow('surface', surface)
    # 发现未知的区域
    surface_fg = np.uint8(surface)
    cv.imshow('surface_bin', surface_fg)
    unknown = cv.subtract(sure_bg,surface_fg)
    # 标记标签
    ret, markers = cv.connectedComponents(surface_fg)
    # 添加一个标签到所有标签，这样确保背景不是0，而是1
    markers = markers + 1
    # 令未知区域为零
    markers[unknown == 255] = 0
    markers = cv.watershed(img, markers)
    img[markers == -1] = [255, 0, 0]
    cv.imshow('result', img)


img = cv.imread('CV-Pictures/lung.jpg', cv.IMREAD_REDUCED_COLOR_2)
# 本案例给出的待分割肺部图片看起来貌似像灰#度图，其实是三通道的图（大家可以通过查看其shape属性验证，由于图像较大所以读入时让其以原图像的1/2尺寸显示）

cv.namedWindow('img',cv.WINDOW_AUTOSIZE)
cv.imshow('img',img)
watershed_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()
