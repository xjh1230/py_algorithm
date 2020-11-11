#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2020/11/11 15:41
# @Software: PyCharm
# @File    : list_node.py

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def gen_link(arr, pos):
    if len(arr) == 0: return None
    head = ListNode(arr[0])
    pre = head
    cycle = None
    for i in range(1, len(arr)):
        cur = ListNode(arr[i])
        if pos == i:
            cycle = cur
        pre.next = cur
        pre = cur
    if cycle is not None:
        pre.next = cycle
    return head


def print_link(head):
    while head is not None:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    head = gen_link(arr, 1)
    print_link(head)
