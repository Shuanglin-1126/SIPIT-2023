# 模板匹配法
import os.path
import cv2
from skimage import io, color
import numpy as np
import time
st1 = time.time()
st = time.time()
from create_template_library import geometry_feature_tem, SIFT_feature_tem, label_tem, hu_feature_tem
en = time.time()
print("标准位姿特征提取消耗时间：{}".format(en - st))
from Feature_generation import *


# 模板匹配： 参数是 1.模板图像地址  2.待匹配图像地址
# 已知的是变压器的型号，需要匹配当前型号变压器的视图

def get_feature_by_type():

    feature = np.array(geometry_feature_tem)
    SIFT_feature = np.array(SIFT_feature_tem)
    label = np.array(label_tem)
    hu_feature = np.array(hu_feature_tem)

    return feature, SIFT_feature, label, hu_feature


def calculate_input_pic_feature(path):
    """
    跟据图片地址，读取图片，计算图片特征
    :param path: 待检测图片地址 类型 str
    :return: pic_feature: 待检测图片特征向量
    """
    if not os.path.exists(path):
        return
    else:
        img_01 = io.imread(path)
        img_01 = color.rgb2gray(img_01)
        pic_feature = feature_create(img_01)
    return pic_feature


def cal_SIFT_sim(img1, img2):

    # 创建匹配器
    bf = cv2.BFMatcher()

    # 遍历标准位姿SIFT矩阵
    # 关键点匹配,通过计算两张图像提取的描述子之间的距离
    matches = bf.knnMatch(img1["descriptors"], img2["descriptors"], k=2)
    top_results1 = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            top_results1.append(m)

    # 记录图2和图1匹配的关键点
    matches2 = bf.knnMatch(img2["descriptors"], img1["descriptors"], k=2)
    top_results2 = []
    for m, n in matches2:
        if m.distance < 0.7 * n.distance:
            top_results2.append(m)

    # 从匹配的关键点中选择出有效的匹配
    # 确保匹配的关键点信息在图1和图2以及图2和图1是一致的
    top_results = []
    for m1 in top_results1:
        m1_query_idx = m1.queryIdx
        m1_train_idx = m1.trainIdx

        for m2 in top_results2:
            m2_query_idx = m2.queryIdx
            m2_train_idx = m2.trainIdx

            if m1_query_idx == m2_train_idx and m1_train_idx == m2_query_idx:
                top_results.append(m1)

    # 计算图像之间的相似度
    # 通过计算两张图片之间的匹配的关键点的个数来计算相似度
    image_sim = len(top_results) / min(len(img1["keypoints"]), len(img2["keypoints"]))
    return image_sim


def caculate_similarity(geometry_feature_map, SIFT_feature_map, hu_feature_map, label_map, feature_vector):
    """
    计算待检测工件特征向量与特征矩阵中标准位姿特征向量的距离
    :param geometry_feature_map: type型号变压器不同视图标准位姿的几何特征矩阵
    :param label_map: type型号变压器视图标签
    :param feature_vector: 待检测工件的特征向量
    :return: 最小距离的视图编号
    """
    #计算几何特征偏差
    distance = np.sum(np.abs(geometry_feature_map - feature_vector["geometry_features"]) / geometry_feature_map, axis=1,
                      keepdims=True)
    #计算hu矩偏差
    hu_distance = np.sum(np.abs((hu_feature_map - feature_vector["hu_features"]) / hu_feature_map), axis=1,keepdims=True)

    # 计算SIFT特征偏差
    SIFT_sim = []
    for SIFT in SIFT_feature_map:
        sim = cal_SIFT_sim(SIFT, feature_vector["SIFT_features"])
        SIFT_sim.append(sim)
    SIFT_sim = np.array(SIFT_sim).reshape((len(SIFT_sim), 1))

    #分别计算三种特征判定的准确率
    hu_distance = np.array(hu_distance).reshape((len(hu_distance), 1))
    label_1 = int(label_map[np.argmin(distance, axis=0)])
    label_2 = int(label_map[np.argmax(SIFT_sim, axis=0)])
    label_3 = int(label_map[np.argmin(hu_distance, axis=0)])

    # 1000与10分别是SIFT特征和几何特征的权重，SIFT相似度求出后基本为小数，而几何特征值相对来说远远大于SIFT特征
    # 因此加入了权重来平衡两者，负号是因为几何特征相似度是越小越相似，SIFT相似度是越大越相似，因此乘以-1来反转
    feature = -1000 * SIFT_sim + distance * 1
    label = int(label_map[np.argmin(feature, axis=0)])
    return label_1, label_2, label_3, label


def interface_template_matching(path):
    """
    图形界面调用的接口
    :param type: 变压器型号 1-7的int类型
    :param path: 待检测图片地址 类型 str
    :return: view_num: 视图编号
    """
    geometry_feature_map, SIFT_feature_map, label_map, hu_feature_map = get_feature_by_type()
    feature_vector = calculate_input_pic_feature(path)
    labels = []
    labels = caculate_similarity(geometry_feature_map, SIFT_feature_map, hu_feature_map, label_map, feature_vector)
    # 从label中获取视图
    #assert labels[3].size == 1, "计算出错，最小距离的视图个数不为 1！"

    return labels


if __name__ == '__main__':
    st = time.time()
    labels = interface_template_matching(r"F:\毕设\实验\变压器数据集\03\34.bmp")
    print(str(labels[3]))
    en = time.time()
    print("单张图片消耗时间：{}".format(en - st))
    en1 = time.time()
    print("单张图执行总时间：{}".format(en1 - st1))
