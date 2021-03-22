#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2021/3/22 16:58
# @Software: PyCharm
# @File    : l14_longest_common_prefix.py

class Solution:
    def longestCommonPrefix(self, strs) -> str:

        if len(strs) < 1:
            return ''
        if len(strs) == 1:
            return strs[0]
        res, i, j, c_0 = '', 1, 0, len(strs[0])
        while True:
            if i == len(strs):
                i = 1
                res += strs[0][j]
                j += 1
            if len(strs[i]) > j and j < c_0 and strs[i][j] == strs[0][j]:
                i += 1
            else:
                break
        return res


if __name__ == '__main__':
    s = Solution()
    strs = ["flower", "flow", "flight"]
    print(s.longestCommonPrefix(strs))
