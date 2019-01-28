#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xm1230
# datetime:2019/1/24 20:24
# software: PyCharm

import math


class Solution:
    def __init__(self):
        self.ERROR_RANGE = 1e-6

        self.dic = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b',
                    12: 'c',
                    13: 'd', 14: 'e', 15: 'f'}

        self.dic_ni = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11,
                       'c': 12,
                       'd': 13, 'e': 14, 'f': 15}

    def sqrt(self, n):
        y = 1.0
        while abs(y * y - n) > self.ERROR_RANGE:
            y = (y + n / y) / 2
        return y

    def bin2(self, n):
        t = 2
        if n < t:
            return n
        result = ''
        while n > t - 1:
            result = str(n % t) + result
            n = math.floor(n / t)
        return str(n) + result

    def oct8(self, n):
        t = 8
        if n < t:
            return n
        result = ''
        while n > t - 1:
            result = str(n % t) + result
            n = math.floor(n / t)
        return str(n) + result

    def toHex(self, n):
        '''
        10转16进制
        :param n:
        :return:
        '''
        if n >= 0:
            t = 16
            if n < t:
                return self.dic[n]
            result = ''
            while n > t - 1:
                result = self.dic[n % t] + result
                n = math.floor(n / t)
            result = self.dic[n] + result
        else:
            tmp = str(self.bin2(-n))
            # 补0
            for i in range(32 - len(tmp)):
                tmp = '0' + tmp
            print(''.join(tmp), '2进制补0')
            tmp = [i for i in tmp]
            count = 31
            # 取反
            for i in range(len(tmp)):
                tmp[i] = '0' if tmp[i] == '1' else '1'
            print(''.join(tmp), '取反')
            # +1
            while count > 0:
                if tmp[count] == '0':
                    tmp[count] = '1'
                    break
                else:
                    tmp[count] = '0'
                    count -= 1
            print(''.join(tmp), '+1')
            # 第一位为1
            tmp = ['1'] + tmp[1:]
            print(''.join(tmp), '第一位为1')
            result = ''.join(tmp)
            # 转为16进制
            tmp16 = ''
            for i in range(8):
                tmp2 = ''
                for j in range(4):
                    tmp2 = result[(i + 1) * 4 - j - 1] + tmp2
                tmp16 = tmp16 + self.toHex(self.int10(tmp2, 2))
                # print(tmp16, tmp2, i, j)
            result = tmp16
        return result

    def int10(self, n, e=2):
        count = len(str(n)) - 1
        result = 0
        for i in str(n):
            result = result + self.dic_ni[i] * (e ** count)
            count -= 1
        return result


if __name__ == '__main__':
    c = Solution()
    # for i in range(1, 160):
    #     tmp = tohex(i)
    #     print(tmp, i, int10(tmp, 16))
    print(c.toHex(-2))
    # print(c.toHex(-1))
    # for i in range(10, 30):
    #     tmp = sqrt(i)
    #     tmp2 = i ** 0.5
    #     print(tmp, tmp2, i, tmp * tmp)
