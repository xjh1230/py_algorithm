# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 10:25
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : search_range.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
        给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

        你的算法时间复杂度必须是 O(log n) 级别。

        如果数组中不存在目标值，返回 [-1, -1]。
        '''
        pass
    def searchRange(self, nums, target):
        find = -1
        if len(nums) == 0:
            return [find, find]
        begin, end = 0, len(nums) - 1
        while begin <= end:
            mid = (begin + end) // 2
            if nums[mid] < target:
                begin = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                find = mid
                break
        begin = end = find
        if find != -1:
            while begin > 0:
                if nums[begin - 1] == target:
                    begin -= 1
                else:
                    break
            while end < len(nums) - 1:
                if nums[end + 1] == target:
                    end += 1
                else:
                    break
        return [begin, end]


if __name__ == '__main__':
    s = Solution()
    arr = [1, 3]
    print(s.searchRange(arr, 1))
    print(s.searchRange(arr, 3))
    arr = [1]
    print(s.searchRange(arr, 8))
    print(s.searchRange(arr, 0))
    print(s.searchRange(arr, 8))
    print(s.searchRange(arr, 5))
    print(s.searchRange(arr, 10))
    print(s.searchRange(arr, 11))
