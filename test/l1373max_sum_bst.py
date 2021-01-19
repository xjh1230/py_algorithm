#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2021/1/19 10:26
# @Software: PyCharm
# @File    : l1373max_sum_bst.py


import data_structure.leecode_tree_node as ltn
from data_structure.leecode_tree_node import TreeNode
import sys


class Solution:
    def maxSumBST(self, root) -> int:
        global maxSum
        maxSum = 0

        def traverse(child):
            '''
            [
            是否是bst,
            最小值，
            最大值，
            和
            ]
            :param root:
            :return:
            '''
            global maxSum
            if child is None:
                return [1, sys.maxsize, -(sys.maxsize - 1), 0]
            left_li = traverse(child.left)
            right_li = traverse(child.right)
            res = [0 for i in range(4)]
            if left_li[0] == 1 and right_li[0] == 1 and child.val < right_li[1] and child.val > left_li[2]:
                res[0] = 1
                res[1] = min(child.val, left_li[1])
                res[2] = max(child.val, right_li[2])
                res[3] = left_li[3] + right_li[3] + child.val
                maxSum = max(maxSum, res[3])
            else:
                res[0] = 0
            return res

        traverse(root)
        return maxSum


if __name__ == '__main__':
    s = Solution()
    # li = [1, 4, 3, 2, 4, 2, 5, None, None, None, None, None, None, 4, 6] #20
    # li = [4, 3, None, 1, 2] #2
    # li = [2, 1, 3] #6
    # li = [-4, -2, -5]  # 0
    li = [5, 4, 8, 3, None, 6, 3]  # 7
    root = ltn.gen_tree(li)
    print(s.maxSumBST(root))
