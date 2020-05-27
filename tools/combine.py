#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2020/5/25 11:12
# @Software: PyCharm
# @File    : combine.py

import os
import chardet


class Solution:
    def __init__(self):
        """
        """

        pass

    def combine(self):
        path = 'mingan'
        path_dir = os.listdir(path)
        i = 1
        li = []
        for p in path_dir:
            f = open(os.path.join(path, p), 'rb')  # 先用二进制打开
            data = f.read()  # 读取文件内容
            file_encoding = chardet.detect(data).get('encoding')
            f = open(os.path.join(path, p), 'r', encoding=file_encoding)
            line = f.readline()
            while line:
                li.append(line.encode('utf8').decode('utf8').replace(',', ''))
                line = f.readline()

        new_file = 'topath.txt'
        f = open(os.path.join(path, new_file), 'w')
        f.writelines(li)
        return len(li)


if __name__ == '__main__':
    s = Solution()
    print(s.combine())
