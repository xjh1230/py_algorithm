# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 16:52
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : triangle.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        '''
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
https://leetcode-cn.com/problems/triangle/
        '''
        pass

    def minimumTotal(self, triangle) -> int:
        '''
        思路：从最后第二层开始，每次保存当前元素与下一行2个元素和的最小值
        :param triangle:
        :return:
        '''
        count = len(triangle)
        if count <= 0:
            return 0
        li = triangle.pop()
        while triangle:
            tmp = []
            for i, v in enumerate(triangle[-1]):
                min_v = min(v + li[i], v + li[i + 1])
                tmp.append(min_v)
            li = tmp
            triangle.pop()
        return min(li)


if __name__ == '__main__':
    li = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    s = Solution()
    print(s.minimumTotal(li))
