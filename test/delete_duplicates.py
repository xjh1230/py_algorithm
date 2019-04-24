# -*- coding: utf-8 -*-
# @Time    : 2019/4/24 10:10
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : delete_duplicates.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        head = self.get_next(head)
        res = head
        while head:
            head.next = self.get_next(head.next)
            head = head.next
        return res

    def get_next(self, head):
        cur = None
        while head:
            if head.next and head.val == head.next.val:
                cur = head.next
                head = head.next.next
            else:
                if cur and head.val == cur.val:
                    cur = head
                    head = head.next
                else:
                    break
        return head


def generate_node(li):
    head = None
    res = None
    for i in li:
        if head:
            head.next = ListNode(i)
            head = head.next
        else:
            head = ListNode(i)
            res = head
    return res


def print_node(head):
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    li = [0, 1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7]
    n = generate_node(li)
    s = Solution()
    res = s.deleteDuplicates(n)
    print_node(res)
