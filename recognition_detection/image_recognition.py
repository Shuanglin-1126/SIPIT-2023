from skimage import io, color
import numpy as np
import cv2
from matplotlib import pyplot as plt
from Feature_generation import *
from match_template import *


def img_recognition(path):
    labels = []
    labels = interface_template_matching(path)
    print("变压器型号：   ", labels[3])
    label = int(labels[3])
    return label


