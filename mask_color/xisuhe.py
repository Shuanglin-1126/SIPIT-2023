import cv2
import numpy as np
from skimage import io
from Feature_generation import *
from matplotlib import pyplot as plt

img = io.imread(r'F:\毕设\实验\bianyaqi2\xisuhe\right_top\1.bmp')
# 高斯滤波器
blur3 = cv2.GaussianBlur(img, (5, 5), 0)
# 双边滤波器，同时考虑像素的空间位置和邻域的像素灰度相似性，在滤波的同时较好的保留图片的边缘
blur4 = cv2.bilateralFilter(img, 9, 75, 75)
# 将图像从RGB颜色空间转到HSV颜色空间
hsv = cv2.cvtColor(blur4, cv2.COLOR_BGR2HSV)
# 颜色阈值分割
low_blue = np.array([0, 0, 0])
high_blue = np.array([160, 90, 50])
mask = cv2.inRange(hsv, low_blue, high_blue)
r, c = mask.shape
mask_01 = cv2.resize(mask, (int(r/2), int(c/2)))

res = cv2.bitwise_and(img, img, mask=mask)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
dst = cv2.morphologyEx(res, cv2.MORPH_CLOSE, kernel)
dst = cv2.morphologyEx(dst, cv2.MORPH_CLOSE, kernel)
dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(dst, 10, 255, 0)  # 二值化
img_02, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
j = 0
cnt_1 = []
cnt_area = np.abs(cv2.contourArea(cnt, True))
for i in range(1, len(contours)):
    area = np.abs(cv2.contourArea(contours[i], True))
    if area > cnt_area:
        cnt = contours[i]
        j = i
        cnt_area = area
cnt_1.append(j)
for i in range(1, len(contours)):
    if i == cnt_1[0]:
        continue
    area = np.abs(cv2.contourArea(contours[i], True))
    if cnt_area - area <= 2000:
        cnt_1.append(i)
#print(cnt_1)
rect = []
box = []
clSobRGB = cv2.cvtColor(dst, cv2.COLOR_GRAY2RGB)  # 灰度图像变RGB，才可以在此基础上画出轮廓
for i in range(0, len(cnt_1)):
    rect_1 = cv2.minAreaRect(contours[cnt_1[i]])
    box_1 = cv2.boxPoints(rect_1)
    box_1 = np.int0(box_1)
    img = cv2.drawContours(clSobRGB, [box_1], 0, (255, 0, 0), 3)  # 画最小外接矩形
    img = cv2.drawContours(img, [contours[cnt_1[i]]], 0, (0, 255, 0), 3)  # 画出轮廓
    rect.append(rect_1)
    box.append(box_1)
plt.figure(1)
plt.imshow(img)
plt.show()


