#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2020/7/22 15:40
# @Software: PyCharm
# @File    : l104_max_depth.py


from data_structure.leecode_tree_node import TreeNode, gen_tree, print_tree

from collections import deque


class Solution:
    def maxDepth1(self, root) -> int:
        '''
        深度优先
        :param root:
        :return:
        '''
        res = 0
        if root is not None:
            res += max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return res

    def maxDepth(self, root) -> int:
        '''
        广度优先
        :param root:
        :return:
        '''
        q = deque([root])
        res = 0
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node:
                    q.extend([node.left, node.right])
            res += 1
        return res - 1


if __name__ == '__main__':
    s = Solution()
    li = [3, 9, 20, None, None, 15, 7]
    t = gen_tree(li)
    res = s.maxDepth(t)
    print(res)
