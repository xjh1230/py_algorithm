#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/12/10 16:14
# @Software: PyCharm
# @File    : remove_duplicates.py

class Solution:
    def __init__(self):
        '''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
        '''

    def removeDuplicates(self, nums) -> int:
        if len(nums) <= 1:
            return len(nums)
        start, end = 1, len(nums)
        pre_i, pre_v = 1, nums[0]
        while start < end:
            if pre_v != nums[start]:
                pre_v = nums[start]
                if pre_i != start:
                    nums[pre_i] = pre_v
                pre_i += 1
            start += 1
        return pre_i

    def removeDuplicates2(self, nums, size) -> int:
        '''
        给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        :param nums:
        :param size:
        :return:
        '''
        if len(nums) <= 1 or len(nums) < size:
            return len(nums)
        start, end = 1, len(nums)
        pre_i, pre_v, count = 1, nums[0], 1
        while start < end:
            if pre_v == nums[start]:
                if count < size:
                    count += 1
                    nums[pre_i] = pre_v
                    pre_i += 1
            elif pre_v < nums[start]:
                pre_v = nums[start]
                nums[pre_i] = pre_v
                pre_i += 1
                count = 1
            start += 1
        return pre_i


if __name__ == '__main__':
    s = Solution()
    li = [0, 0, 1, 1, 2, 3, 4, 5, 5, 6]
    i = s.removeDuplicates(li)
    print(li, i)

    li = [0, 0, 1, 1, 1, 1, 2, 3, 3, 3, 3, 4]
    i = s.removeDuplicates2(li, 2)
    print(li, i)

    li = [1, 1, 1, 2, 2, 3]
    i = s.removeDuplicates2(li, 2)
    print(li, i)
    li = [1, 2, 3, 4, 5]
    i = s.removeDuplicates2(li, 2)
    print(li, i)
    li = [1]
    i = s.removeDuplicates2(li, 2)
    print(li, i)
    li = [1, 1, 1, 1, 1]
    i = s.removeDuplicates2(li, 2)
    print(li, i)
