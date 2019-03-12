# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 11:26
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : add-two-numbers.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def get_from_arr(self, li):
        tmp = self
        for i in range(len(li) - 1):
            tmp.val = li[i]
            tmp.next = ListNode(0)
            tmp = tmp.next
        tmp.val = li[-1]

    @staticmethod
    def rever_link(l):
        prev_node = None
        cur_node = l
        next_node = l.next
        while cur_node:
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
            if next_node:
                next_node = next_node.next
        return prev_node

    def __str__(self):
        tmp = self
        s = ''
        while tmp:
            s += str(tmp.val)
            tmp = tmp.next
        return s


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/add-two-numbers/
        给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
        '''
        pass

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        tmp = result
        last = None
        prev = 0
        while l1 and l2:
            val = prev + l1.val + l2.val
            prev, tmp.val = divmod(val, 10)
            last = tmp
            tmp.next = ListNode(0)
            l1, l2, tmp = l1.next, l2.next, tmp.next
        if l1:
            tmp.val, tmp.next = l1.val + prev, l1.next
        elif l2:
            tmp.val, tmp.next = l2.val + prev, l2.next
        else:
            if prev > 0:
                last.next.val += prev
            else:
                last.next = None
        last = last.next
        while last:
            if last.val > 9:
                last.val = last.val % 10
                if not last.next:
                    last.next = ListNode(1)
                else:
                    last.next.val += 1
                    last = last.next
            else:
                break
        return result


if __name__ == '__main__':
    # s = Solution()
    # l1 = ListNode(5)
    # l1.next = ListNode(9)
    # l1.next = ListNode(9)
    #
    # l2 = ListNode(5)
    #
    # l3 = s.addTwoNumbers(l1, l2)
    # print(l3)
    l = ListNode(0)
    l.get_from_arr([3, 4, 5])
    print(l)
    l = ListNode.rever_link(l)
    print(l)
