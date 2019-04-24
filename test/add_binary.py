# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 15:57
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : add_binary.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/add-binary/
        给定两个二进制字符串，返回他们的和（用二进制表示）。

        输入为非空字符串且只包含数字 1 和 0。

        示例 1:

        输入: a = "11", b = "1"
        输出: "100"
        示例 2:

        输入: a = "1010", b = "1011"
        输出: "10101"
        '''

    def addBinary1(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary(self, a: str, b: str) -> str:
        from functools import reduce
        m, n, res = len(a), len(b), []
        if m > n:
            a, b = b, a
        a = '0' * (len(b) - len(a)) + a
        flag = 0
        for i in range(len(a) - 1, -1, -1):
            if int(a[i]) & int(b[i]):
                res.append(flag)
                flag = 1
            else:
                tmp = int(a[i]) | int(b[i])
                if tmp & flag == 1:
                    res.append(0)
                else:
                    res.append(flag | tmp)
                    flag = 0
        if flag == 1:
            res.append(flag)
        return reduce(lambda x, y: str(y) + str(x), res, '')
