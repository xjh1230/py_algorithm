#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/12/9 16:40
# @Software: PyCharm
# @File    : remove_element.py


class Solution:
    def __init__(self):
        """
        """
        pass

    def removeElement(self, nums, val: int) -> int:
        removed = 0
        count = len(nums)
        for i in range(count):
            index = i - removed
            if nums[index] == val:
                nums.pop(index)
                removed += 1
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    s.removeElement(nums, val)
    print(nums)

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    s.removeElement(nums, val)
    print(nums)
