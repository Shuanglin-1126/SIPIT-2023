import math
import cv2
import numpy as np
import time
import os.path
import matplotlib.pyplot as plt
from skimage import io, color
from Feature_generation import *
from image_recognition import *
from image_world import *


def img_detection(path):
    label = img_recognition(path)
    img_1 = io.imread(path)
    img_1 = color.rgb2gray(img_1)
    me = img_d1(img_1, label)
    points = []
    angles = []
    ranges = []
    for i in range(0, len(me)):
        print("第", (i+1), "个变压器：   ")
        me_1 = me[i]
        x, y , x_1, y_1= image_world(me_1[0][0], me_1[0][1])
        x = float(x)
        x1 = int(x_1 * 100) / 100
        y = float(y)
        y1 = int(y_1 * 100) / 100
        point = (x1, y1)
        print("中心点坐标：   ", point)
        me_1[1] = int(me_1[1] * 100) / 100
        me_1[2] = int(me_1[2] * 100) / 100
        print("机械手旋转角度：   ", me_1[1])
        print("机械手张开距离：   ", me_1[2])
        points.append(point)
        angles.append(me_1[1])
        ranges.append(me_1[2])
    return points, angles, ranges

time_st = time.time()
path = r"F:\毕设\实验\图像分类与检测\变压器检测图像\1个变压器\1.bmp"

img_detection(path)
time_end = time.time()
print(time_end-time_st)