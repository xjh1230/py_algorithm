#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xm1230
# datetime:2019/3/27 20:58
# software: PyCharm

from tack import SStack
from tree_node import BinTNode


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


class DictOptBinTree(DicBinTree):
    def __init__(self, seq):
        '''
        最佳二叉树字典
        :param seq:
        '''
        DicBinTree.__init__(self)
        data = sorted(seq)
        self._root = DictOptBinTree.builtOBT(data, 0, len(data) - 1)

    @staticmethod
    def builtOBT(data, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        left = DictOptBinTree.builtOBT(data, start, mid - 1)
        right = DictOptBinTree.builtOBT(data, mid + 1, end)
        # s = (1, 2)
        # ss = Assoc(*s)
        return BinTNode(Assoc(*data[mid]), left, right)


import random

if __name__ == '__main__':
    # d = DicBinTree()
    # li = [random.randint(1, 100) for i in range(20)]
    # for i, v in enumerate(li):
    #     d.insert(v, i)
    # for i in d.values():
    #     print(i, end=',')
    s = 'abcdefghijklmn'
    seq = [(i, s[i]) for i in range(1, 14)]
    d = DictOptBinTree(seq)
    for i in d.values():
        print(i)
    print(seq)
