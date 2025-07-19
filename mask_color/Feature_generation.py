import math
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 开操作
def imgopen(image):
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
    dst = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    return dst

# 闭操作
def imgclose(image):
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dst = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    return dst

# Sobel算子 图像梯度
def imgSobel(image):
    Sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    Sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    Sobelx = cv2.convertScaleAbs(Sobelx)  # 转回uint8
    Sobely = cv2.convertScaleAbs(Sobely)
    Sobelxy = cv2.addWeighted(Sobelx, 0.5, Sobely, 0.5, 0)
    return Sobelxy

# canny算子 边缘检测
def imgcanny(image):
    blur = cv2.GaussianBlur(image, (5, 5), 0)  # 高斯滤波
    canny = cv2.Canny(blur, 50, 150)  # 50是最小阈值,150是最大阈值
    return canny

def sys_moments(img):
    """
    opencv_python自带求矩以及不变矩的函数
    :param img: 灰度图像，对于二值图像来说就只有两个灰度0和255
    :return: 返回以10为底对数化后的hu不变矩
    """
    moments = cv2.moments(img)#返回的是一个字典，三阶及以下的几何矩（mpq）、中心矩(mupq)和归一化的矩(nupq)
    humoments = cv2.HuMoments(moments)#根据几何矩（mpq）、中心矩(mupq)和归一化的矩(nupq)计算出hu不变矩
    # 因为直接计算出来的矩可能很小或者很大，因此取对数好比较,这里的对数底数为e,通过对数除法的性质将其转换为以10为底的对数
    humoment = (np.log(np.abs(humoments)))/np.log(10)
    return humoment

# SIFT特征点提取
def extract_sift_feature(img):
    """
    提取图形中的SIFT点信息
    :param img: 待检测图像
    :return: 传入图像的特征信息
    """
    img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')
    sift = cv2.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(img, None)
    return keypoints, descriptors

def feature_create(image):
    image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')
    Sobelxy = imgSobel(image)
    cannySob = imgcanny(Sobelxy)
    opSob = imgopen(cannySob)
    clSob = imgclose(opSob)
    keypoints, descriptors = extract_sift_feature(image)

    # ROI 最小外接矩形 和 轮廓
    ret, thresh = cv2.threshold(clSob, 127, 255, 0)  # 二值化
    img_02, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    cnt_area = np.abs(cv2.contourArea(cnt, True))
    for i in range(1, len(contours)):
        area = np.abs(cv2.contourArea(contours[i], True))
        if area > cnt_area:
            cnt = contours[i]
            cnt_area = area

    rect = cv2.minAreaRect(cnt)

    # 轮廓面积 and 最小外接矩形面积
    S = cv2.contourArea(cnt, oriented=False)  # 轮廓面积
    width, height = rect[1]  # 最小外接矩形长宽
    ROI_area = width * height  # 最小外接矩形面积

    # 轮廓周长
    c = cv2.arcLength(curve=cnt, closed=True)

    # 几何参数
    m = c ** 2 / (4 * math.pi * S)  # 圆形度m 目标接近圆形的程度
    R = S / ROI_area  # 矩形度R 目标物体对外接矩形的填充程度
    r = height / width  # 长宽比r 最小外接矩形的高与宽之比

    #图像的hu矩
    hu = []
    hu = sys_moments(clSob)

    geometry_features = [S, ROI_area, width, height, c, m, R, r]
    SIFT_features = {"keypoints": keypoints, "descriptors": descriptors}
    features = {
        "geometry_features": geometry_features,
        "SIFT_features": SIFT_features,
        "hu_features": hu
    }
    return features

def get_flag(label):
    flag_1 = 0
    if label == 1:
        flag_1 = 0
    if label == 2:
        flag_1 = 0
    if label == 3:
        flag_1 = 0
    if label == 4:
        flag_1 = 0
    if label == 5:
        flag_1 = 20000
    if label == 6:
        flag_1 = 0
    if label == 7:
        flag_1 = 0
    flag = flag_1
    return flag


def draw(img, result, label):
    # 下面几个参数，可能需要根据自己的数据进行调整
    x = int(result[0][0])  # 矩形框的中心点x
    y = int(result[0][1])  # 矩形框的中心点y
    angle = result[2]  # 矩形框的倾斜角度（长边相对于水平）
    width, height = int(result[1][0]), int(result[1][1])  # 矩形框的宽和高
    if width < height:
        width = int(result[1][1])
        height = int(result[1][0])
        angle = angle + 90
    if label == 4 or label == 7:
        height = 100
    else:
        width = 100
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
    if label == 4 or label == 7:
        angle = angle - 90
        height = width
    angle = angle + 90
    if angle >= 180:
        angle = angle - 180
    me.append(angle)
    me.append(height)
    return me

def img_d1(image, label):
    image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')
    Sobelxy = imgSobel(image)
    cannySob = imgcanny(Sobelxy)
    opSob = imgopen(cannySob)
    clSob = imgclose(opSob)

    # ROI 最小外接矩形 和 轮廓
    ret, thresh = cv2.threshold(clSob, 127, 255, 0)  # 二值化
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
    flag_1 = get_flag(label)
    for i in range(1, len(contours)):
        if i == cnt_1[0]:
            continue
        area = np.abs(cv2.contourArea(contours[i], True))
        if cnt_area - area <= flag_1:
            cnt_1.append(i)
    #print(cnt_1)
    rect = []
    box = []
    me = []
    img = cv2.cvtColor(clSob, cv2.COLOR_GRAY2RGB)  # 灰度图像变RGB，才可以在此基础上画出轮廓
    for i in range(0, len(cnt_1)):
        rect_2 = []
        rect_1 = cv2.minAreaRect(contours[cnt_1[i]])
        box_1 = cv2.boxPoints(rect_1)
        box_1 = np.int0(box_1)
        img = cv2.drawContours(img, [box_1], 0, (255, 0, 0), 3)  # 画最小外接矩形
        img = cv2.drawContours(img, [contours[cnt_1[i]]], 0, (0, 255, 0), 3)  # 画出轮廓
        me_1 = draw(img, rect_1, label)
        rect.append(rect_1)
        box.append(box_1)
        me.append(me_1)
    plt.imshow(img)
    plt.show()
    img = cv2.resize(img, (400, 350))
    cv2.imwrite('01.jpg', img)
    return me

def img_r(image):
    image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')

    Sobelxy = imgSobel(image)
    cannySob = imgcanny(Sobelxy)
    opSob = imgopen(cannySob)
    clSob = imgclose(opSob)

    ret, thresh = cv2.threshold(clSob, 127, 255, 0)  # 二值化
    img_02, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    cnt_area = np.abs(cv2.contourArea(cnt, True))
    for i in range(1, len(contours)):
        area = np.abs(cv2.contourArea(contours[i], True))
        if area > cnt_area:
            cnt = contours[i]
            cnt_area = area

    rect = cv2.minAreaRect(cnt)

    # 轮廓面积 and 最小外接矩形面积
    S = cv2.contourArea(cnt, oriented=False)  # 轮廓面积
    width, height = rect[1]  # 最小外接矩形长宽
    ROI_area = width * height  # 最小外接矩形面积

    # 轮廓周长
    c = cv2.arcLength(curve=cnt, closed=True)

    # 几何参数
    m = c ** 2 / (4 * math.pi * S)  # 圆形度m 目标接近圆形的程度
    R = S / ROI_area  # 矩形度R 目标物体对外接矩形的填充程度
    r = height / width  # 长宽比r 最小外接矩形的高与宽之比

    # 图像的hu矩
    hu = []
    hu = sys_moments(clSob)

    row, col, h = image.shape
    for i in range(0, row):
        for j in range(0, col):
            test_point = (j, i)
            flag = cv2.pointPolygonTest(cnt, test_point, False)
            flag = int(flag)
            if flag < 0:
                image[i, j] = 0
    keypoints, descriptors = extract_sift_feature(image)


    geometry_features = [S, ROI_area, width, height, c, m, R, r]
    SIFT_features = {"keypoints": keypoints, "descriptors": descriptors}
    features = {
        "geometry_features": geometry_features,
        "SIFT_features": SIFT_features,
        "hu_features": hu
    }
    return features

