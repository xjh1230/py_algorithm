#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/10/30 20:04
# @Software: PyCharm
# @File    : l528_pick_index.py

import random
import bisect


class Solution1:

    def __init__(self, w):
        '''
        此方法保证100%按照概率分配
        :param w:
        '''
        self.w = w
        self.gen()
        self.dic = {}
        self.cur = 0
        self.max = len(w)
        self.sum = sum(w)

    def gen(self):
        li = []
        tmp = 0
        for i, v in enumerate(self.w):
            tmp += v
            li.append(tmp)
        self.li = li

    def pickIndex(self) -> int:
        if self.cur == sum(self.w):
            self.dic = {}
            self.cur = 0
        self.cur += 1
        rd = random.randint(0, self.sum)
        index = bisect.bisect_left(self.li, rd)
        # index = random.randint(0, self.max - 1)
        count = self.dic.get(index, 0)
        if count < self.w[index]:
            self.dic[index] = count + 1
            return index
        else:
            tmp = 0
            while tmp < self.max:
                if tmp != index:
                    count = self.dic.get(tmp, 0)
                    if count < self.w[tmp]:
                        self.dic[tmp] = count + 1
                        return tmp
                tmp += 1


class Solution:
    def __init__(self, w):
        self.check, cur, total = [], 0, sum(w)
        for x in w:
            cur += x
            self.check.append(cur / total)

    def pickIndex(self) -> int:
        return bisect.bisect(self.check, random.random())


if __name__ == '__main__':
    li = [1,3]
    # li = [3, 7, 3, 6, 7, 8]
    s = Solution(li)
    res = []
    for i in range(4):
        res.append(s.pickIndex())
    print(res)
