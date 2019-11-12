#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/11/11 16:06
# @Software: PyCharm
# @File    : l75_sort_colors.py


class Solution:
    def __init__(self):
        """
        """
        pass

    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i0 = i1 = i2 = count = len(nums)
        c0 = c1 = c2 = 0
        for index in range(count):
            v = nums[index]
            if v == 0:
                if i1 < index:  # 交换0,1值，同时更新0,1索引
                    nums[i1], nums[index] = 0, 1
                    if i0 == count:
                        i0 = i1
                    i1 = index - c1 - c2 + 1
                    if index > i2:  # 交换1,2值,同时更新2索引
                        nums[index], nums[i2] = 2, 1
                        i2 += 1
                elif i2 < index:
                    nums[i2], nums[index] = 0, 2  # 交换0,2值,同时更新0,2索引
                    if i0 == count:
                        i0 = i2
                    i2 = index - c2 + 1
                if i0 == count:
                    i0 = index
                c0 += 1
            elif v == 1:
                if i2 < index:  # 交换1,2值,同时更新1,2索引
                    nums[index], nums[i2] = 2, 1
                    if i1 == count:
                        i1 = i2
                    i2 = index - c2 + 1
                if i1 == count:
                    i1 = index
                c1 += 1
            else:
                if i2 == len(nums):
                    i2 = index
                c2 += 1
        return nums


if __name__ == '__main__':
    sc = Solution()
    nums = [1, 2, 0, 1, 1, 2, 2, 0, 0, 1, 2, 0, 2, 2, 1, 1, 0]
    # nums = [2, 0, 2, 1, 1, 0]
    # nums = [0, 2, 2, 2, 0, 2, 1, 1]
    # nums = [1, 1, 0, 0, 1, 1]
    # nums = [2, 2, 2, 0, 0, 2, 0, 2, 0, 2]
    print(sc.sortColors(nums))
