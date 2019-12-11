#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/12/9 16:12
# @Software: PyCharm
# @File    : move_zero.py


class Solution:
    def __init__(self):
        """
        给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
        """
        pass

    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start_z, end_z, i = -1, -1, 0
        while (i < len(nums)):
            if (nums[i] == 0):
                if start_z == -1:
                    start_z = i
                    end_z = i
                else:
                    end_z = i
            if (nums[i] != 0):
                if (start_z != -1):
                    span = end_z - start_z
                    for j in range(0, span + 1):
                        if nums[i] == 0:
                            break
                        nums[start_z], nums[i] = nums[i], nums[start_z]
                        i += 1
                        start_z += 1
                        end_z += 1
                        if i >= len(nums):
                            return
                else:
                    i += 1
            else:
                i += 1


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    print(nums)
    nums = [1, 1, 1]
    s.moveZeroes(nums)
    print(nums)

    nums = [0, 0, 0]
    s.moveZeroes(nums)
    print(nums)
    nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
    s.moveZeroes(nums)
    print(nums)
