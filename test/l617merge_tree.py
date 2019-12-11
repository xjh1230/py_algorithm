#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/11/22 13:09
# @Software: PyCharm
# @File    : l617merge_tree.py

from data_structure.leecode_tree_node import TreeNode
from data_structure.leecode_tree_node import gen_tree
from data_structure.leecode_tree_node import print_tree
import math


class Solution:
    def __init__(self):
        """
        """
        pass

    def mergeTrees1(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def get_one(li):
            if li:
                return li.pop(0)
            else:
                return None

        if not t1 and not t2:
            return None

        res_t = TreeNode(0)
        left_stack = [t1]
        right_stack = [t2]
        res_stack = [res_t]
        while left_stack or right_stack:
            left = get_one(left_stack)
            right = get_one(right_stack)
            cur = get_one(res_stack)
            if cur:
                if left:
                    cur.val += left.val
                    left_stack.append(left.left)
                    left_stack.append(left.right)
                else:
                    left_stack.append(None)
                    left_stack.append(None)
                if right:
                    cur.val += right.val
                    right_stack.append(right.left)
                    right_stack.append(right.right)
                else:
                    right_stack.append(None)
                    right_stack.append(None)
                if (left and left.left) or (right and right.left):
                    cur.left = TreeNode(0)
                else:
                    cur.left = None
                res_stack.append(cur.left)
                if (left and left.right) or (right and right.right):
                    cur.right = TreeNode(0)
                else:
                    cur.right = None
                res_stack.append(cur.right)
        return res_t

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        '''
        超时没通过
        :param t1:
        :param t2:
        :return:
        '''

        def to_li(t: TreeNode):
            if t:
                stack = [t]
                res = []
                dep = 0
                while stack:
                    c = len(stack)
                    tmp = [None] * 2 * c
                    has_next = False
                    i = 0
                    dep += 1
                    while stack:
                        cur = stack.pop(0)
                        if cur:
                            has_next = True
                            res.append(cur.val)
                            tmp[i * 2] = cur.left
                            tmp[i * 2 + 1] = cur.right
                        else:
                            res.append(None)
                            tmp[i * 2] = None
                            tmp[i * 2 + 1] = None
                        i += 1
                    if has_next:
                        stack = tmp
                res = res[:int(math.pow(2, dep - 1)) - 1]
                return res

        def add_li(li1, li2):
            def my_sum(l, r):
                if l is None:
                    return r
                elif r is None:
                    return l
                return l + r

            c1 = len(li1)
            c2 = len(li2)
            if c1 > c2:
                sub = c1 - c2
                li2.extend([None] * sub)
            elif c2 > c1:
                sub = c2 - c1
                li1.extend([None] * sub)
            res = [my_sum(li1[i], li2[i]) for i in range(len(li1))]
            return res

        def to_tree(li):
            root = TreeNode(li.pop(0))
            stack = [root]
            while li:
                cur = stack.pop(0)
                if cur:
                    v_left = li.pop(0)
                    v_right = li.pop(0)
                    left = TreeNode(v_left) if v_left is not None else None
                    right = TreeNode(v_right) if v_right is not None else None
                    cur.left = left
                    cur.right = right
                    stack.append(left)
                    stack.append(right)
                else:
                    li.pop(0)
                    li.pop(0)
                    stack.append(None)
                    stack.append(None)
            return root

        if t1 is None:
            return t2
        if t2 is None:
            return t1
        li1 = to_li(t1)
        li2 = to_li(t2)
        res = add_li(li1, li2)
        return to_tree(res)


if __name__ == '__main__':
    sc = Solution()
    li1 = [4, -9, 5, None, -1, None, 8, -6, 0, 7, None, None, -2, None, None, None, None, -3]
    li2 = [5]
    t1 = gen_tree(li1)
    t2 = gen_tree(li2)
    t = sc.mergeTrees(t1, t2)
    print(print_tree(t, True))
    t = sc.mergeTrees1(t1, t2)
    print(print_tree(t, True))
    # [9,-9,5,null,-1,null,8,-6,0,7,null,null,-2,null,null,null,null,-3]
