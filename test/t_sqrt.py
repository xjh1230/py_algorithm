#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xm1230
# datetime:2019/1/24 20:24
# software: PyCharm

import math

ERROR_RANGE = 1e-6


def sqrt(n):
    y = 1.0
    while abs(y * y - n) > ERROR_RANGE:
        y = (y + n / y) / 2
    return y


def bin2(n):
    t = 2
    if n < t:
        return n
    result = '';
    while n > t - 1:
        result = str(n % t) + result
        n = math.floor(n / t)
    return str(n) + result


def oct8(n):
    t = 8
    if n < t:
        return n
    result = '';
    while n > t - 1:
        result = str(n % t) + result
        n = math.floor(n / t)
    return str(n) + result


def int10(n, e=2):
    count = len(str(n))-1
    result = 0
    for i in str(n):
        result = result + int(i) * (e ** count)
        count -= 1
    return result


if __name__ == '__main__':
    for i in range(1, 160):
        tmp = oct8(i)
        print(tmp, i, int10(tmp, 8))
    # for i in range(10, 30):
    #     tmp = sqrt(i)
    #     tmp2 = i ** 0.5
    #     print(tmp, tmp2, i, tmp * tmp)
