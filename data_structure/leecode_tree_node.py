#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/11/6 16:44
# @Software: PyCharm
# @File    : leecode_tree_node.py

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


def print_tree(t):
    li = []
    stack = [t]
    while stack:
        cur = stack.pop(0)
        if cur:
            li.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            else:
                # li.append(None)
                pass
            if cur.right:
                stack.append(cur.right)
            else:
                # li.append(None)
                pass
    return li


if __name__ == '__main__':
    li = [1, None, 2, 3, 4, 5, 6]
    t = gen_tree(li)
    li2 = print_tree(t)
    print(li, li2)
