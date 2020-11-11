#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2020/11/11 15:37
# @Software: PyCharm
# @File    : l141link_list_cycle.py

from data_structure.list_node import ListNode, gen_link


class Solution:
    def __init__(self):
        '''

        '''

    def hasCycle(self, head):
        if head is None:
            return False
        slow = head
        fast = head.next
        while fast is not None and slow is not None:
            if fast.val == slow.val:
                return True
            slow = slow.next
            fast = fast.next
            if fast is None:
                return False
            fast = fast.next
        return False


if __name__ == '__main__':
    s = Solution()
    arr = [3, 2, 0, -4]
    pos = 2
    head = gen_link(arr, pos)
    print(s.hasCycle(head))
