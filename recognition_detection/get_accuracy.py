import os
import time
import numpy as np
from match_template import interface_template_matching


def get_data_list(path, data):
    """
    获取地址下的所有文件
    :param path: 文件地址
    :param data: 保存文件地址
    :return: 传入地址下的所有文件 type: list
    """
    filelist = os.listdir(path)
    for file in filelist:
        filepath = os.path.join(path, file)
        if os.path.isdir(filepath):
            data = get_data_list(filepath, data=data)
        else:
            data.append(filepath)

    return data


def get_gtlabel(path):
    """
    获取数据真实标签
    :param: path: 数据根目录
    :return: gt_label: 包含数据地址和标签的字典
    """
    data_path = []
    # 获取数据文件地址
    data_path = get_data_list(path, data=data_path)
    gt_labels = []
    # 分割获取label
    for i, filepath in enumerate(data_path):
        temp = filepath.split('.')[0]
        # 获取标签
        if temp[-1] == '0':
            # 剔除标准位姿标签
            continue
        label = int(temp[-3])
        label = str(label)
        dic = {
            "path": filepath,
            "label": label
        }
        gt_labels.append(dic)

    return gt_labels


# 读取所有文件进行预测计算正确率
def caculate_accuracy():
    """
    读取所有文件计算预测正确率
    :return: accuracy: 模板匹配正确率
    """
    gt_label = get_gtlabel(r"F:\毕设\实验\图像分类与检测\标定前图像\单个变压器")
    num_acc_10 = 0
    num_acc_20 = 0
    num_acc_30 = 0
    num_acc_40 = 0
    true_type_label = []
    prediction_type_label = []
    for i, label in enumerate(gt_label):
        path = label["path"]
        gt_label_1 = label["label"]
        prediction_labels = interface_template_matching(path)
        if str(prediction_labels[3]) == gt_label_1:
            num_acc_40 = num_acc_40 + 1
        else:
            temp = path.split('.')[0]
            gt_label_2 = temp[-3] + temp[-1]
            true_type_label.append(gt_label_2)
            prediction_type_label.append(prediction_labels[3])
        false_list = {
            "true_type_label": true_type_label,
            "prediction_type_label": prediction_type_label
        }
        if str(prediction_labels[0]) == gt_label_1:
            num_acc_10 = num_acc_10 + 1
        if str(prediction_labels[1]) == gt_label_1:
            num_acc_20 = num_acc_20 + 1
        if str(prediction_labels[2]) == gt_label_1:
            num_acc_30 = num_acc_30 + 1
    num_acc_1 = num_acc_10 / len(gt_label)
    num_acc_2 = num_acc_20 / len(gt_label)
    num_acc_3 = num_acc_30 / len(gt_label)
    num_acc_4 = num_acc_40 / len(gt_label)
    return num_acc_1, num_acc_2, num_acc_3, num_acc_4, false_list


st = time.time()
acc_1, acc_2, acc_3, acc_4, False_list = caculate_accuracy()
print("总体准确率：  ", acc_1)
print("总体准确率：  ", acc_2)
print("总体准确率：  ", acc_3)
print("总体准确率：  ", acc_4)
print(False_list["true_type_label"])
print(False_list["prediction_type_label"])
en = time.time()
#print("所有图像消耗时间：{}".format(en - st))

