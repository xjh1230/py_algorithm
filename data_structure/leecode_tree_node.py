#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/11/6 16:44
# @Software: PyCharm
# @File    : leecode_tree_node.py
import math


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def gen_tree(li):
    if len(li) == 0:
        return None
    t = TreeNode(li[0])
    li_tree = [t]
    cur = li_tree.pop(0)
    set_left = False
    set_right = False
    for i in li[1:]:
        if not set_left:
            cur.left = gen_tree_node(i, li_tree)
            set_left = True
        elif not set_right:
            cur.right = gen_tree_node(i, li_tree)
            set_right = True
        else:
            cur = li_tree.pop(0)
            cur.left = gen_tree_node(i, li_tree)
            set_left = True
            set_right = False
    return t


def gen_tree_node(s, li):
    if s is None:
        return s
    else:
        t = TreeNode(s)
        li.append(t)
        return t


def print_tree(t, has_none=False):
    li = []
    stack = [t]
    while stack:
        cur = stack.pop(0)
        if cur:
            li.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
            if has_none:
                if not cur.left:
                    stack.append(None)
                if not cur.right:
                    stack.append(None)
        elif has_none:
            li.append(None)

    return li


def to_li(t: TreeNode):
    if t:
        stack = [t]
        res = []
        while stack:
            cur = stack.pop(0)
            if cur:
                stack.append(cur.left)
                stack.append(cur.right)
                res.append(cur.val)
            else:
                res.append(None)
        return res
    else:
        return None


def to_fullli(t: TreeNode):
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


if __name__ == '__main__':
    def test_li(li):
        t = gen_tree(li)
        li2 = print_tree(t, has_none=True)
        return li2


    li = [1, None, 2, 3, 4, 5, 6]
    li = [4, -9, 5, None, -1, None, 8, -6, 0, 7, None, None, -2, None, None, None, None, -3]
    t = gen_tree(li)
    li2 = print_tree(t, True)
    print(li2)
