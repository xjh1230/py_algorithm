#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2021/3/19 16:28
# @Software: PyCharm
# @File    : l501_find_mode_in_tree.py

import data_structure.leecode_tree_node as ltn


class Solution:
    def __init__(self):
        '''
        给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树

        '''

    def findMode_1(self, root: ltn.TreeNode):
        stack, dict, max_c, res, = [], {}, 0, []
        if root is None:
            return res
        stack.append(root)
        while len(stack) > 0:
            tmp = stack.pop(0)
            c = dict.get(tmp.val, 0)
            dict[tmp.val] = c + 1
            max_c = max(max_c, c + 1)
            if tmp.left is not None:
                stack.append(tmp.left)
            if tmp.right is not None:
                stack.append(tmp.right)
        for k, v in dict.items():
            if v == max_c:
                res.append(k)
        return res

    def findMode_2(self, root: ltn.TreeNode):
        '''
        利用bst树的特性（数据是有序的 Morris 中序遍历）
        找到前置节点（左子树的最右节点），将其右子树置为当前节点，遍历就不用回退到当前节点，直接用右子树来遍历下一节点
        :param root:
        :return:
        '''
        count = max_c = 0
        res = []
        base = None

        def update(cur):
            nonlocal base, count, max_c, res
            if cur == base:
                count += 1
            else:
                count = 1
                base = cur
            if count == max_c:
                res.append(cur)
            if count > max_c:
                max_c = count
                res = [cur]

        cur_node = root
        while cur_node is not None:
            if cur_node.left is None:
                update(cur_node.val)
                cur_node = cur_node.right
                continue
            pre = cur_node.left
            while pre.right is not None and pre.right != cur_node:
                pre = pre.right  # 找到最右节点，即前置节点
            if pre.right is None:  # 找到最右节点
                pre.right = cur_node  # 将前置节点置为当前节点的父节点
                cur_node = cur_node.left  # 中序遍历，先访问左节点
            else:  # 最右节点是当前节点
                pre.right = None
                update(cur_node.val)
                cur_node = cur_node.right
        return res

    def findMode(self, root: ltn.TreeNode):
        count = max_c = 0
        prev = None
        res = []

        def searchBST(tree: ltn.TreeNode):
            nonlocal count, max_c, prev, res
            if tree is None:
                return
            searchBST(tree.left)
            if prev is None:
                count = 1
            elif prev.val == tree.val:
                count += 1
            else:
                count = 1
            prev = tree
            if count == max_c:
                res.append(tree.val)
            elif count > max_c:
                max_c = count
                res = [tree.val]
            searchBST(tree.right)
            return

        searchBST(root)
        return res


if __name__ == '__main__':
    s = Solution()
    data = [6, 2, 8, 0, 4, 7, 9, None, None, 2, 6]
    t = ltn.gen_tree(data)
    print(s.findMode(t))
