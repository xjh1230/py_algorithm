# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 15:34
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : tree_node.py
# @Software: PyCharm


class Assoc:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key


class BinTNode:
    def __init__(self, assoc, left=None, right=None):
        self.data = assoc
        self.left = left
        self.right = right


class AVLNode(BinTNode):
    def __init__(self, data):
        BinTNode.__init__(data)
        self.bf = 0
