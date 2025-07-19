import cv2
import numpy as np
from skimage import io
from matplotlib import pyplot as plt
import math

def draw1(img, result, label):
    # 下面几个参数，可能需要根据自己的数据进行调整
    x = int(result[0][0])  # 矩形框的中心点x
    y = int(result[0][1])  # 矩形框的中心点y
    angle = result[2]  # 矩形框的倾斜角度（长边相对于水平）
    print(angle)
    width, height = int(result[1][0]), int(result[1][1])  # 矩形框的宽和高
    if width < height:
        width = int(result[1][1])
        height = int(result[1][0])
        angle = angle - 90
    if label == 4 or label == 7 or label == 2:
        height = 140
    else:
        width = 140
    print(angle)
    anglePi = angle * math.pi / 180.0  # 计算角度
    cosA = math.cos(anglePi)
    sinA = math.sin(anglePi)

    x1 = x - 0.5 * width
    y1 = y - 0.5 * height

    x0 = x + 0.5 * width
    y0 = y1

    x2 = x1
    y2 = y + 0.5 * height

    x3 = x0
    y3 = y2

    x0n = (x0 - x) * cosA - (y0 - y) * sinA + x
    y0n = (x0 - x) * sinA + (y0 - y) * cosA + y

    x1n = (x1 - x) * cosA - (y1 - y) * sinA + x
    y1n = (x1 - x) * sinA + (y1 - y) * cosA + y

    x2n = (x2 - x) * cosA - (y2 - y) * sinA + x
    y2n = (x2 - x) * sinA + (y2 - y) * cosA + y

    x3n = (x3 - x) * cosA - (y3 - y) * sinA + x
    y3n = (x3 - x) * sinA + (y3 - y) * cosA + y

    # 根据得到的点，画出矩形框

    cv2.line(img, (int(x0n), int(y0n)), (int(x1n), int(y1n)), (0, 0, 255), 6)
    cv2.line(img, (int(x1n), int(y1n)), (int(x2n), int(y2n)), (0, 0, 255), 6)
    cv2.line(img, (int(x2n), int(y2n)), (int(x3n), int(y3n)), (0, 0, 255), 6)
    cv2.line(img, (int(x0n), int(y0n)), (int(x3n), int(y3n)), (0, 0, 255), 6)

    me = []
    me.append(result[0])
    if label == 4 or label == 7 or label == 2:
        angle = angle - 90
        length = width
    else:
        length = height
    angle = -angle
    if angle >= 90:
        angle = angle - 180
    if angle <= -90:
        angle = angle + 180
    me.append(angle)
    height_world = int(length * 1000) / 218 * 12 / 1000
    me.append(height_world)
    return me


img = io.imread(r'F:\bianyaqi2\xisuhe\right_top\1.bmp')
# 高斯滤波器
blur3 = cv2.GaussianBlur(img, (5, 5), 0)
# 双边滤波器，同时考虑像素的空间位置和邻域的像素灰度相似性，在滤波的同时较好的保留图片的边缘
blur4 = cv2.bilateralFilter(img, 9, 75, 75)
plt.figure(1)
plt.imshow(blur4)

# 将图像从RGB颜色空间转到HSV颜色空间
hsv = cv2.cvtColor(blur4, cv2.COLOR_BGR2HSV)
# 颜色阈值分割
plt.figure(2)
plt.imshow(hsv)
low_blue = np.array([0, 0, 0])
high_blue = np.array([160, 90, 50])
mask = cv2.inRange(hsv, low_blue, high_blue)


res = cv2.bitwise_and(blur4, blur4, mask=mask)
plt.figure(3)
plt.imshow(mask)
plt.figure(4)
plt.imshow(mask, cmap='gray')
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
dst = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
dst = cv2.morphologyEx(dst, cv2.MORPH_CLOSE, kernel)
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
    #img = cv2.drawContours(clSobRGB, [box_1], 0, (255, 0, 0), 3)  # 画最小外接矩形
    img = cv2.drawContours(clSobRGB, [contours[cnt_1[i]]], 0, (0, 255, 0), 3)  # 画出轮廓
    #me_1 = draw1(img, rect_1, 5)
    rect.append(rect_1)
    box.append(box_1)
plt.figure(5)
plt.imshow(img)
plt.show()


