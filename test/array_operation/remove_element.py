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
        给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:

给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。
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
