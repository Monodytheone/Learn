import cv2

img = cv2.imread("model.png")
cv2.imshow("no_detected_face", img)  # 显示未检出人脸时的原始图片
# 加载识别正面人脸的级联分类器
faceCascade = cv2.CascadeClassifier("cascades\\haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(img, 1.3)  # 识别出所有人脸
for (x, y, w, h) in faces:  # 遍历所有人脸的区域
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 5)  # 在图像中人脸的位置绘制方框
cv2.imshow("detected_face", img)  # 显示最终处理的效果
cv2.waitKey()
cv2.destroyAllWindows()