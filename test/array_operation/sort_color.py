#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/12/19 16:17
# @Software: PyCharm
# @File    : sort_color.py

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end, end_0, start_1, start_2, count_1 = len(nums) - 1, -1, -1, -1, 0
        for i in range(end, -1, -1):
            if nums[i] == 2:
                start_2 = i
            else:
                break
        if start_2 == 0:
            return
        for i in range(len(nums)):
            if start_2 != -1 and i >= start_2:
                break
            if nums[i] == 2:
                if start_2 == -1:
                    nums[i], nums[end] = nums[end], nums[i]
                    start_2 = end
                else:
                    while nums[start_2 - 1] == 2:
                        start_2 -= 1
                    if start_2 - 1 > end_0 and start_2 - 1 > start_1 + count_1:
                        start_2 -= 1
                    else:
                        break
                    nums[i], nums[start_2] = nums[start_2], nums[i]
            if nums[i] == 1:
                count_1 += 1
                if start_1 == -1:
                    start_1 = i
            if nums[i] == 0:
                end_0 += 1
                if start_1 != -1:
                    nums[i], nums[start_1] = nums[start_1], nums[i]
                    if nums[start_1 + 1] == 1:
                        start_1 += 1
                    else:
                        start_1 = -1


if __name__ == '__main__':
    s = Solution()
    # nums = [0, 2, 2, 2, 0, 2, 1, 1]
    # s.sortColors(nums)
    # print(nums)
    # nums = [2,0,2,1,1,0]
    # s.sortColors(nums)
    # print(nums)
    nums = [0, 2, 1, 2, 0, 2, 0, 1, 2, 2, 2, 1, 1, 1, 0]
    s.sortColors(nums)
    print(nums)
