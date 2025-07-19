import math
import cv2
import numpy as np
import matplotlib.pyplot as plt


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