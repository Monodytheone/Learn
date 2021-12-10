# 首先生成一个矩阵，然后把矩阵作用在变换对象上，.就行了
from cv2 import cv2
import numpy as np


img = cv2.imread(r'C:\Users\Turnip\Desktop\07.png')
cv2.imshow('img', img)
