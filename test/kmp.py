#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/11/6 17:43
# @Software: PyCharm
# @File    : kmp.py


class KMP:
    def __init__(self):
        """
        字符串比较kmp算法
        https://cloud.tencent.com/developer/article/1434241
        """
        self.li = []

    def compare(self, s1, s2):
        i, j, end = 0, 0, len(s1) - len(s2)
        dic = self.getPMT(s2)
        while j < len(s2) and i < len(s1):
            if s1[i] == s2[j]:
                # if j == len(s2) - 1:#找多个匹配
                #     # return i
                #     self.li.append(i)
                #     j = 0
                #     i += 1
                i += 1
                j += 1
            else:
                j = dic[j]
                if j == 0:
                    i += 1
        # print(i, j)
        # return self.li
        return i - 1 if j == len(s2) else 0

    def getPMT(self, search):
        '''
        （Partial Match Table）部分匹配表
        :param search:
        :return:
        '''
        dic = {}
        for i in range(len(search)):
            dic[i] = self.getSST(search[0:i])
        return dic

    def getSST(self, str):
        if len(str) < 2:
            return 0
        before = {}
        for i in range(1, len(str)):
            before[str[0:i]] = 1
        for i in range(1, len(str)):
            tmp = str[i:]
            if tmp in before:
                return len(tmp)
        return 0


if __name__ == '__main__':
    sc = KMP()
    s1 = 'BBC ABCDAB ABCDABCDABDF'
    s2 = 'ABCD'
    res = sc.compare(s1, s2)
    print(sc.li, res, s1[res - len(s2) + 1:res + 1])
    # print(sc.getPMT(s2))
