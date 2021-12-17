'''
实验内容及算法思想：
手机拍照自带各种各样的贴图特效，实际上这些贴图特效就是先定位了人脸位置，然后在人脸相应
的位置覆盖素材实现的。本实验就尝试实现此功能---为人脸添加戴墨镜的额特效。
实验的主要步骤如下：
1、首先编写一个覆盖图片的overlay_img()方法，因为给大家提供的素材中可能包含透明像素，
这些透明像素不可以遮挡人脸，所以在覆盖背景图像时要做判断，忽略所有透明像素。判断一个
像素是否为透明像素，只需将图像从3通道转换为4通道，判断第四通道的alpha（即透明度）值，
alpha值为1表示完全不透明，alpha值为0表示完全透明；
2、创建人脸识别级联分类器，分析出图像中人脸的区域；
3、把墨镜图像按照人脸宽度进行缩放，并覆盖到人脸区域约三分之一的位置。
'''

import cv2

# 覆盖图像
def overlay_img(img, img_over, img_over_x, img_over_y):
    """
    覆盖图像
    :param img: 背景图像
    :param img_over: 覆盖的图像
    :param img_over_x: 覆盖图像在背景图像上的横坐标
    :param img_over_y: 覆盖图像在背景图像上的纵坐标
    :return: 两张图像合并之后的图像
    """
    img_h, img_w, img_p = img.shape  # 背景图像宽、高、通道数
    img_over_h, img_over_w, img_over_c = img_over.shape  # 覆盖图像高、宽、通道数
    if img_over_c == 3:  # 通道数小于等于3
        img_over = cv2.cvtColor(img_over, cv2.COLOR_BGR2BGRA)  # 转换成4通道图像
    for w in range(0, img_over_w):  # 遍历列
        for h in range(0, img_over_h):  # 遍历行
            if img_over[h, w, 3] != 0:  # 如果不是全透明的像素
                for c in range(0, 3):  # 遍历三个通道
                    x = img_over_x + w  # 覆盖像素的横坐标
                    y = img_over_y + h  # 覆盖像素的纵坐标
                    if x >= img_w or y >= img_h:  # 如果坐标超出最大宽高
                        break  # 不做操作
                    img[y, x, c] = img_over[h, w, c]  # 覆盖像素
    return img  # 完成覆盖的图像


face_img = cv2.imread("peoples.png",cv2.IMREAD_REDUCED_COLOR_2)  # 读取人脸图像
cv2.imshow("no_sunglasses_face", face_img)  # 显示未带墨镜的人脸的效果
glass_img = cv2.imread("glass.png", cv2.IMREAD_UNCHANGED)  # 读取眼镜图像，保留图像类型
height, width, channel = glass_img.shape  # 获取眼镜图像高、宽、通道数
# 加载识别正面人脸的级联分类器
face_cascade = cv2.CascadeClassifier("./cascades/haarcascade_frontalface_default.xml")
garyframe = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)  # 转为黑白图像
faces = face_cascade.detectMultiScale(garyframe, 1.3, 5)  # 识别人脸
for (x, y, w, h) in faces:  # 遍历所有人脸的区域
    gw = w  # 眼镜缩放之后的宽度
    gh = int(height * w / width)  # 眼镜缩放之后的高度度
    glass_img = cv2.resize(glass_img, (gw, gh))  # 按照人脸大小缩放眼镜
    overlay_img(face_img, glass_img, x, y + int(h * 1 / 3))  # 将眼镜绘制到人脸上

cv2.imshow("sunglasses_face", face_img)  # 显示最终处理的效果
cv2.waitKey()  # 按下任何键盘按键后
cv2.destroyAllWindows()  # 释放所有窗体
