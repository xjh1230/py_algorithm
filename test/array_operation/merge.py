#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/12/24 14:43
# @Software: PyCharm
# @File    : merge.py

class Solution:
    def __init__(self):
        """
        """
        pass

    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, tmp, p1, p2 = 0, nums1[:m], 0, 0

        while p1 < m and p2 < n:
            a, b = tmp[p1], nums2[p2]
            if a < b:
                nums1[i] = tmp[p1]
                p1 += 1
            elif a > b:
                nums1[i] = nums2[p2]
                p2 += 1
            else:
                nums1[i] = tmp[p1]
                i += 1
                nums1[i] = nums2[p2]
                p2 += 1
                p1 += 1
            i += 1
        while p1 < m:
            nums1[i] = tmp[p1]
            p1 += 1
            i += 1
        while p2 < n:
            nums1[i] = nums2[p2]
            p2 += 1
            i += 1


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1)
