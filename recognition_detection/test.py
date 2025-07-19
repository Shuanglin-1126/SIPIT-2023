from skimage import io, color
from Feature_generation import *

path = r"F:\图像分类与检测\变压器检测图像\3个变压器\2.bmp"
img = io.imread(path)
img = color.rgb2gray(img)
img_r(img)
