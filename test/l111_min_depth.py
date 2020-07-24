#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2020/7/24 9:39
# @Software: PyCharm
# @File    : l111_min_depth.py


from data_structure.leecode_tree_node import TreeNode, gen_tree, print_tree

from collections import deque


class Solution:
    def __init__(self):
        self.count = 0

    def minDepth(self, root) -> int:  # dfs
        self.count += 1
        res = 0
        if root is None:
            return res
        if root.left is None and root.right is None:
            res += 1
        else:
            # 左右子树都不为空，去最小值
            # 左右子树有任何一个为空，取最大值
            res = max(self.minDepth(root.right),
                      self.minDepth(root.left)) + 1 if root.left is None or root.right is None else min(
                self.minDepth(root.left),
                self.minDepth(
                    root.right)) + 1
        return res

    def minDepth2(self, root):

        res = 0
        if root is None:
            return res
        q = deque([root])
        while q:
            self.count += 1
            n = len(q)
            for i in range(n):
                t = q.popleft()
                if t is not None:
                    if t.left is None and t.right is None:
                        return res + 1
                    q.extend([t.left, t.right])
            res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    li = [3, 9, 20, None, None, 15, 7]
    t = gen_tree(li)
    print(s.minDepth(t), s.count)
    s.count = 0
    print(s.minDepth2(t), s.count)
