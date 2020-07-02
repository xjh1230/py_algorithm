#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2020/5/27 17:35
# @Software: PyCharm
# @File    : l974_subarray_sums_div_by_k.py

class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/
        '''
        pass

    def subarraysDivByK(self, A, K) -> int:
        '''
        学习
        https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/solution/you-jian-qian-zhui-he-na-jiu-zai-ci-dai-ni-da-tong/
        '''
        dic = {0: 1}
        preSum = 0
        res = 0
        for i in A:
            preSum = (preSum + i) % K
            if preSum < 0:  # 同余定理
                preSum += K
            if preSum in dic:  # 同一个余数出现第二次表示 从第一次出现到第二次出现中间的那部分子数组和正好就能整除k
                res += dic[preSum]
            if preSum in dic:
                dic[preSum] += 1
            else:
                dic[preSum] = 1
        return res


def fib(n):
    a = 1
    b = 1
    i = 2
    if n <= 2:
        return 1
    else:
        tmp = 0
        while i < n:
            a, b = b, a + b
            i += 1
        return b


if __name__ == '__main__':
    s = fib(100)
    print(s)
