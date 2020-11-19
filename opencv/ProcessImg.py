#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2020/11/19 14:29
# @Software: PyCharm
# @File    : ProcessImg.py

# 注意opencv 版本
# pip install opencv-python==3.4.2.16
# pip install opencv-contrib-python==3.4.2.16
import cv2
import os

save_path = "D:/cut_image/"
source_path = "./img/source1.jpg"


# Mean Shift的优点就在于如果是像背景桌面的浅色纹理，图像分割的过程中相当于将这些小的浮动过滤掉，并且保留相对明显的纸张边缘，结果如下：
# image = cv2.pyrMeanShiftFiltering(image, 25, 10)

def threshold_demo(image):
    # 去噪声+二值化
    dst = cv2.GaussianBlur(image, (3, 3), 0)
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
    # cv.imshow("binary", binary)
    return binary


def canny_demo(image, t, t2):
    '''
    边缘检测
    :param image: 源图片
    :param t: 低于阈值1的像素点会被认为不是边缘
    :param t: 高于阈值2的像素点会被认为是边缘
    :return:
    '''
    canny_output = cv2.Canny(image, t, t2)
    # cv.imshow("canny_output", canny_output)
    return canny_output


class ProcessImg:
    def __init__(self):
        """
        git 地址
        https://github.com/JimmyHHua/opencv_tutorials.git
        https://github.com/JimmyHHua/opencv_tutorials/blob/master/python/code_048/opencv_048.py
        """
        self.out_base = save_path

    def run(self, source_path):
        src = cv2.imread(source_path)
        # cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
        # cv.imshow("input", src)
        binary = threshold_demo(src)
        canny = canny_demo(src, 100, 100 * 4)
        # 轮廓发现
        out, contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # 绘制轮廓
        # for c in range(len(contours)):
        #     cv.drawContours(src, contours, c, (0, 0, 255), 2, 8)
        nrootdir = self.out_base
        if not os.path.isdir(nrootdir):
            os.makedirs(nrootdir)
        for i in range(0, len(contours)):
            x, y, w, h = cv2.boundingRect(contours[i])
            newimage = src[y + 2:y + h - 2, x + 2:x + w - 2]  # 先用y确定高，再用x确定宽  没有黑边框
            # newimage = src[y + 1:y + h - 1, x + 1:x + w - 1]  # 先用y确定高，再用x确定宽  黑边框外边有1的白背景
            # newimage = src[y:y + h, x:x + w]  # 先用y确定高，再用x确定宽    黑边框外边有2的白背景
            # 排除杂项
            if h > 80 and w > 80:
                cv2.imwrite(nrootdir + str(i) + ".png", newimage)
            # if h > 80 and w > 80:
            # if len(newimage) > 75 and len(newimage[0] > 75):
            #     # 轮廓填充颜色
            #     # cv2.rectangle(src, (x, y), (x + w, y + h), (0, 0, 0), 5)
            #     cv2.imwrite(nrootdir + str(i) + ".png", newimage)
            # break


if __name__ == '__main__':
    print(cv2.__version__)
    path = source_path
    p = ProcessImg()
    p.run(path)
