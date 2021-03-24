#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2021/3/22 17:26
# @Software: PyCharm
# @File    : l710_random_pick.py

import random
import bisect


class Solution:

    def __init__(self, N: int, blacklist):
        '''
        映射黑名单到白名单，然后去随机数白名单的长度
        :param N:
        :param blacklist:
        n:1000
        len(b):10
        w_len" 990
        bi < w_len--n:  5
        '''
        b_w_map = {}
        w_len = N - len(blacklist)  # w_len 990
        s_w = set([i for i in range(w_len, N)])  # 990-1000
        s_b = set(blacklist)
        s_w -= s_b
        for i in blacklist:
            if i < w_len:
                b_w_map[i] = s_w.pop()
        self.map = b_w_map
        self.w_len = w_len

    def pick(self):
        t = random.randint(0, self.w_len)
        return self.map.get(t, t)


class Solution2:
    def __init__(self, N: int, blacklist):
        '''
        将黑白名单都排序
        b:[1,3,5]
        w:[0,2,4,6,7]
        r = random(len_m) = 4 白名单中第r个数
        必然是：r+黑名单中小于等于r的个数k(lo索引+1)(即二分查找黑名单中的r)(即跳过了多少个)
        4 + (1 + 1) = 6
        假设结果就是总名单的第x个数
            则：其中有r个白名单，k个黑名单
            若 b[0]>r 则 k = 0 即 r=x
            否则 r不变，二分搜索寻找k。k+r>x(可理解为b[k])（即前x个数里面有<k个黑名单） 则k 往小调整，否则往k大调整（即前x个数里面有>k个黑名单）
        :param N:
        :param blacklist:
        '''
        self.n = N
        self.b = sorted(blacklist)
        self.w_len = N - len(self.b)

    def pick(self):
        r = random.randint(0, self.w_len - 1)
        if len(self.b) == 0 or self.b[0] > r:  # 表示黑名单为空，或者r不在黑名单中（黑中最小的都大于r）
            return r
        lo, hi = 0, len(self.b) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if self.b[mid] > r + mid:  # b[mid]:总数中第mid个(也就是最终的结果)，mid:黑名单中小于b[mid]的个数   r:白名单的中小于b[mid]的个数
                hi = mid - 1
            else:
                lo = mid
        return r + lo + 1


if __name__ == '__main__':
    s = Solution2(5, [0, 2])
    for i in range(20):
        print(s.pick())
        # s.pick()
