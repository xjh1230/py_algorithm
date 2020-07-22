#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2020/7/22 15:32
# @Software: PyCharm
# @File    : l589_preorder.py


class Solution:
    def preorder(self, root):
        res = []
        if root != None:
            res.append(root.val)
            if root.children != None:
                for c in root.children:
                    res.extend(self.preorder(c))
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.preorder(None)
    print(res)
