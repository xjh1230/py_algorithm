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
            # 此时p前面全小于x p和crt之间>x
            while p is not crt:
                y = p.elem
                p.elem = x
                x = y
                p = p.next
            crt.elem = x
            crt = crt.next


def sort(li):
    count = len(li)
    if count <= 1:
        return li
    r = 1
    while r < count:
        i = 0
        tmp = li[r]
        while i < r and li[i] < li[r]:
            i += 1
        while i < r:
            tmp1 = li[i]
            li[i] = tmp
            tmp = tmp1
            i += 1
        li[r] = tmp
        r += 1
    return li


def swap(li, i, j):
    li[i], li[j] = li[j], li[i]


li = [9, 6, 8, 1, 5, 7, 4, 3]
li = sort(li)


# print(li)

def josephus_L(n, k, m):
    people = list(range(1, n + 1))
    i = k - 1
    for num in range(n, 0, -1):
        i = (i + m - 1) % num
        print(people.pop(i), end=(', ' if num > 1 else '\n'))
    return


josephus_L(10, 2, 7)

if __name__ == '__main__':
    l = LLink()
    for i in range(10):
        l.preappend(i)
    l.preappend(4)
    l.preappend(2)
    for i in l.elements():
        print(i.elem)
    l.sort1()
    print('*' * 40)
    for i in l.elements():
        print(i.elem)
