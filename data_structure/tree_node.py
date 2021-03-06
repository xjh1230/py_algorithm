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


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def print_tree(node, has_none=True):
        li = []
        li_node = [node]
        while len(li_node) > 0:
            tmp = li_node.pop(0)
            if tmp:
                li.append(tmp.val)
                li_node.append(tmp.left)
                li_node.append(tmp.right)
            else:
                if has_none:
                    li.append(None)
        for i in range(len(li) - 1, -1, -1):
            if li[i] == None:
                li.pop(i)
            else:
                break
        return li

    @staticmethod
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
                cur.left = t.gen_tree_node(i, li_tree)
                set_left = True
            elif not set_right:
                cur.right = t.gen_tree_node(i, li_tree)
                set_right = True
            else:
                cur = li_tree.pop(0)
                cur.left = t.gen_tree_node(i, li_tree)
                set_left = True
                set_right = False
        return t

    @staticmethod
    def gen_tree_node(s, li):
        if s is None:
            return s
        else:
            t = TreeNode(s)
            li.append(t)
            return t