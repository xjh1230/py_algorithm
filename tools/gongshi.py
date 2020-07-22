#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2020/7/18 16:40
# @Software: PyCharm
# @File    : gongshi.py

class gongshi:
    def __init__(self):
        """
        """
        pass


def quadratic(a, b, c):
    tmp = b ** 2 - 4 * a * c
    if tmp >= 0 and a != 0:
        x1 = (-1 * b + tmp ** 0.5) / (2 * a)
        x2 = (-1 * b - tmp ** 0.5) / (2 * a)
        print(x1, x2)
    else:
        print('无解')


if __name__ == '__main__':
    quadratic(2, 3, 1)
