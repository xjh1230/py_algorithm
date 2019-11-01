#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/10/31 19:42
# @Software: PyCharm
# @File    : l926min_flips_mono_incr.py


class Solution:
    def __init__(self):
        '''
        如果一个由 '0' 和 '1' 组成的字符串，是以一些 '0'（可能没有 '0'）后面跟着一些 '1'（也可能没有 '1'）的形式组成的，那么该字符串是单调递增的。
我们给出一个由字符 '0' 和 '1' 组成的字符串 S，我们可以将任何 '0' 翻转为 '1' 或者将 '1' 翻转为 '0'。
返回使 S 单调递增的最小翻转次数。
https://leetcode-cn.com/problems/flip-string-to-monotone-increasing
10001->2 ->00000
        '''

    def minFlipsMonoIncr1(self, str1: str) -> int:
        pre = '0'
        zero = 0
        one = 0
        dic = {0: 0, 1: 0, 10: 0}
        start = 0
        end = len(str1) - 1
        while str1[start] == '0' or str1[end] == '1':  # 排除左边的0和右边的1最终会剩下101010这样的一组数据
            if start == len(str1) - 1 or end == 0:
                return 0
            if str1[start] == '0':
                start += 1
            if str1[end] == '1':
                end -= 1
        for i in range(start, end + 1):  # 1010 最终会有 0000 1111 01这种形式,分别计算不同形式的最小值
            if zero == 0:
                if str1[i] == pre:
                    zero += 1
                else:
                    one += 1
            else:
                if str1[i] == pre:
                    zero += 1
                else:
                    self.set_dic(dic, one, zero)
                    zero = 0
                    one = 1
        self.set_dic(dic, one, zero)
        return min(dic[0], dic[1], dic[10])

    def set_dic(self, dic, one, zero):
        tmp_zero = dic[0] + one
        tmp_one = min(dic[0], dic[10]) + zero
        tmp_zero_one = min(dic[0], dic[1], dic[10]) + zero
        dic[0] = tmp_zero
        dic[1] = tmp_one
        dic[10] = tmp_zero_one

    def minFlipsMonoIncr(self, S):
        res = var = S.count('0')
        for num in S:
            if num == '1':
                var += 1
            elif num == '0':
                var -= 1
            res = min(res, var)
        return res


if __name__ == '__main__':
    s = Solution()
    # str1 = '00110'
    # print(s.minFlipsMonoIncr(str1), str1)
    str1 = '0001111000'
    print(s.minFlipsMonoIncr(str1), str1)
    print(s.minFlipsMonoIncr1(str1), str1)
    # str1 = '00011000'
    # print(s.minFlipsMonoIncr(str1), str1)
    # str1 = '0001110001'
    # print(s.minFlipsMonoIncr(str1), str1)
    # str1 = '1100001'
    # print(s.minFlipsMonoIncr(str1), str1)
    # str1 = '111'
    # print(s.minFlipsMonoIncr(str1), str1)
    # str1 = '000'
    # print(s.minFlipsMonoIncr(str1), str1)
    # str1 = '1001010110'
    # print(s.minFlipsMonoIncr(str1), str1)
