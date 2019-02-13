# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 15:41
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : find_median_sorted_arrays.py
# @Software: PyCharm

import math


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        返回两个数组合并后的中间值，如果合并后个数是奇数的 返回中间数，偶数的，返回 (half+half+1)/2
        """
        m = len(nums1)
        n = len(nums2)
        half = (m + n) / 2
        new_nums = nums1 + nums2
        new_nums = sorted(new_nums)
        print(new_nums)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError
        if (m + n) % 2 == 0:
            half = int(half)
            return (new_nums[half - 1] + new_nums[half]) / 2
        else:
            return new_nums[math.floor(half)]

    def test(self):
        num1 = [3]
        num2 = [-2, -1]
        print(self.findMedianSortedArrays(num1, num2))


if __name__ == '__main__':
    s = Solution()
    s.test()
