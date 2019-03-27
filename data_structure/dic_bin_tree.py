#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xm1230
# datetime:2019/3/27 20:58
# software: PyCharm

from tack import SStack


class Assoc:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class BinTNode:
    def __init__(self, assoc, left=None, right=None):
        self.data = assoc
        self.left = left
        self.right = right


class DicBinTree:
    def __init__(self):
        '''
        二叉树实现字段
        '''
        self._root = None

    # 判空
    def is_empty(self):
        return self._root is None

    # 搜索
    def search(self, key):
        '''
        搜索
        :param key:
        :return:
        '''
        bt = self._root
        while bt is not None:
            entry = bt.data
            if entry.key > key:
                bt = bt.left
            elif entry.key < key:
                bt = bt.right
            else:
                return entry.value
        return None

    def insert(self, key, value):
        bt = self._root
        node = BinTNode(Assoc(key, value))
        if bt is None:
            self._root = node
            return
        while True:
            entry = bt.data
            if key < entry.key:
                if bt.left is None:
                    bt.left = node
                    return
                bt = bt.left
            elif key > entry.key:
                if bt.right is None:
                    bt.right = node
                    return
                bt = bt.right
            else:
                bt.data.value = value
                return

    def values(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t)
                t = t.left
            t = s.pop()
            yield t.data.key, t.data.value
            t = t.right


import random

if __name__ == '__main__':
    d = DicBinTree()
    li = [random.randint(1, 100) for i in range(20)]
    for i, v in enumerate(li):
        d.insert(v, i)
    for i in d.values():
        print(i, end=',')
