#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xm1230
# datetime:2019/3/19 22:15
# software: PyCharm

class LNode:
    def __init__(self, elem, next_):
        self.elem = elem
        self.next = next_


class LLink:
    def __init__(self):
        self.head = None
        self.count = 0

    def preappend(self, elem):
        self.head = LNode(elem, self.head)
        self.count += 1

    def elements(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def sort1(self):
        if self.head is None:
            return
        crt = self.head.next
        while crt is not None:
            x = crt.elem
            p = self.head
            while p is not crt and p.elem <= x:
                p = p.next
            while p is not crt:
                y = p.elem
                p.elem = x
                x = y
                p = p.next
            crt.elem = x
            crt = crt.next


if __name__ == '__main__':
    l = LLink()
    for i in range(10):
        l.preappend(i)
    for i in l.elements():
        print(i.elem)
    l.sort1()
    print('*' * 40)
    for i in l.elements():
        print(i.elem)
