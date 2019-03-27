#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xm1230
# datetime:2019/3/27 21:22
# software: PyCharm

class StackUnderflow(ValueError):
    pass


class SStack:
    def __init__(self):
        '''
        栈 顺序表实现
        '''
        self._elems_ = []

    def is_empty(self):
        return self._elems_ == []

    def top(self):
        if self.is_empty():
            raise StackUnderflow('in SStack.top()')
        return self._elems_[-1]

    def push(self, elem):
        self._elems_.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackUnderflow('in SStack.pop()')
        return self._elems_.pop()
