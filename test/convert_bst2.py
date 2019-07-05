# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 15:22
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : convert_bst2.py
# @Software: PyCharm

from functools import reduce


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/convert-bst-to-greater-tree/
        给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

例如：

输入: 二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-bst-to-greater-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        '''
        self.prev = 0

    def get_node(self, li):
        if len(li) == 0:
            return None
        node = TreeNode(li.pop(0))
        li_node = [node]
        while len(li) > 0:
            tmp_node = li_node.pop(0)
            tmp_node.left = TreeNode(li.pop(0))
            li_node.append(tmp_node.left)
            if len(li) > 0:
                tmp_node.right = TreeNode(li.pop(0))
                li_node.append(tmp_node.right)
        return node

    def print_node(self, node):
        li = []
        li_node = [node]
        while len(li_node) > 0:
            tmp = li_node.pop(0)
            if tmp:
                li.append(tmp.val)
                li_node.append(tmp.left)
                li_node.append(tmp.right)
        return li

    def convertBST(self, root):
        self.calcNode(root)
        return root

    def calcNode(self, node):
        if node == None:
            return
        self.calcNode(node.right)
        node.val += self.prev
        self.prev = node.val
        self.calcNode(node.left)


if __name__ == '__main__':
    s = Solution()
    li = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9]
    # [7, 4, 11, 2, 5, 9, 13]    [40,49,24,51,45,33,13]
    #  [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]  [92,114,54,119,105,75,29,120,117,110,99,84,65,42,15]
    # [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9]  [53, 75, 26, 80, 66, 36, 14, 81, 78, 71, 60, 45]
    # res = s.convertBST(li)
    # res = s.get_node(1, 4)
    node = s.get_node(li)
    node = s.convertBST(node)
    res = s.print_node(node)
    print(res)
