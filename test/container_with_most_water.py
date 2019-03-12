# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 16:58
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : container_with_most_water.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/container-with-most-water/
        '''
        pass

    def maxArea(self, height):
        area = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = max(area, self.getArea(l, height[l], r, height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return area

    def getArea(self, i1, v1, i2, v2):
        return (i2 - i1) * min(v1, v2)


if __name__ == '__main__':
    s = Solution()
    arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(s.maxArea(arr))
