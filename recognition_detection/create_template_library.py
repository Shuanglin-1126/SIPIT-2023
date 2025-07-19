# 生成模板库
import os.path
import numpy as np
import time
from skimage import io, color
from Feature_generation import *

geometry_feature_tem = []
SIFT_feature_tem = []
label_tem = []
hu_feature_tem = []
st = time.time()
i = 1
while i < 8:
    # 取出7个工件的标准视图进行特征提取
    sti = str(i)
    path = r'F:\图像分类与检测\标定前图像\单个变压器'
    file = '0' + '.bmp'
    pathfile = os.path.join(path, sti, file)
    if not os.path.exists(pathfile):
        break
    else:
        img_01 = io.imread(pathfile)
        img_01 = color.rgb2gray(img_01)
        features = feature_create(img_01)
        geometry_feature_tem.append(features["geometry_features"])
        SIFT_feature_tem.append(features["SIFT_features"])
        hu_feature_tem.append(features["hu_features"])
        label_tem.append(i)
    i = i + 1

geometry_feature_tem = np.array(geometry_feature_tem)
SIFT_feature_tem = np.array(SIFT_feature_tem)
hu_feature_tem = np.array(hu_feature_tem)
label_tem = np.array(label_tem)
