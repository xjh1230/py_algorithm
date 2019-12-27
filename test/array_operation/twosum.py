#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/12/24 15:07
# @Software: PyCharm
# @File    : twosum.py

class Solution:
    def __init__(self):
        """
        """
        pass

    def twoSum(self, numbers, target: int):
        res = []
        dic = {}
        for i in range(len(numbers)):
            dic[numbers[i]] = i
        i = 0
        for num in numbers:
            tmp = target - num
            if tmp in dic:
                # if tmp in dic and i + 1 not in res and i != dic[tmp]:
                return [i + 1, dic[tmp] + 1]
            # res.extend([i + 1, dic[tmp] + 1])
            i += 1
        return res


import re




if __name__ == '__main__':
    s = Solution()
    arr = [-1, 0]
    target = -1
    res = s.twoSum(arr, target)
    print(res)
