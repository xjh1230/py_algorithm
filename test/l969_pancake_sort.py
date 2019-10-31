#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/10/29 17:29
# @Software: PyCharm
# @File    : l969_pancake_sort.py


class Solution:
    def __init__(self):
        '''
        给定数组 A，我们可以对其进行煎饼翻转：我们选择一些正整数 k <= A.length，然后反转 A 的前 k 个元素的顺序。我们要执行零次或多次煎饼翻转（按顺序一次接一次地进行）以完成对数组 A 的排序。
返回能使 A 排序的煎饼翻转操作所对应的 k 值序列。任何将数组排序且翻转次数在 10 * A.length 范围内的有效答案都将被判断为正确。
https://leetcode-cn.com/problems/pancake-sorting
        '''

    def pancakeSort(self, A):
        res = []
        for x in range(len(A), 1, -1):
            i = A.index(x)
            res.extend([i + 1, x])
            A = A[:i:-1] + A[:i]
            # print(A, i + 1, x)
        return res

    def pancakeSort1(self, A):
        # 每次把最大元素放到最后
        res, target = [], sorted(A)
        if A != target:
            # max_index = self.get_max_index(A) + 1
            max_index = A.index(max(A)) + 1
            if max_index != len(A):
                # if max_index != 1:
                res.append(max_index)
                self.reversed_arr(A, max_index)
                # if len(A) != 1:
                res.append(len(A))
                self.reversed_arr(A, len(A))
            res.extend(self.pancakeSort(A[:len(A) - 1]))
        return res

    def get_max_index(self, arr):
        max, max_index = arr[0], 0
        for i in range(len(arr)):
            if arr[i] > max:
                max = arr[i]
                max_index = i
        return max_index

    def reversed_arr(self, arr, index):
        max = len(arr)
        if max >= index:
            start = 0
            index = index - 1
            while start < index:
                arr[start], arr[index] = arr[index], arr[start]
                start += 1
                index -= 1


if __name__ == '__main__':
    s = Solution()
    li = [3, 2, 4, 1, 7, 5, 6]
    res = s.pancakeSort(li)
    res1 = s.pancakeSort1(li)
    print(res, res1)
