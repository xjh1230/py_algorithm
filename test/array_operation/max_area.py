#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/12/26 17:12
# @Software: PyCharm
# @File    : max_area.py

class Solution:
    def __init__(self):
        """
        """
        pass

    def maxArea(self, height):
        res, l, r = 0, 0, len(height) - 1
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    res = s.maxArea(height)
    print(res)
