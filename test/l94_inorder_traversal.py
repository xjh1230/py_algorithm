#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/11/8 9:47
# @Software: PyCharm
# @File    : l94_inorder_traversal.py


import data_structure.leecode_tree_node as ltn
from data_structure.leecode_tree_node import TreeNode


class Solution:
    def __init__(self):
        """
        给定一个二叉树，返回它的中序 遍历。
        示例:
        输入: [1,null,2,3]
           1
            \
             2
            /
           3

        输出: [1,3,2]
        进阶: 递归算法很简单，你可以通过迭代算法完成吗？
        链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
        """
        pass

    def inorderTraversal(self, root: TreeNode):
        '''
        传统递归  不改变数结构
        :param root:
        :return:
        '''
        res = []
        if root is not None:
            res.extend(self.inorderTraversal(root.left))
            res.append(root.val)
            res.extend(self.inorderTraversal(root.right))
        return res

    def inorderTraversal1(self, root: TreeNode):
        '''
        迭代  不改变树结构
        :param root:
        :return:
        '''
        WHITE, GRAY = 0, 1
        stack = [(WHITE, root)]
        res = []
        while stack:
            color, node = stack.pop()
            if node is not None:
                if color == WHITE:
                    stack.append((WHITE, node.right))
                    stack.append((GRAY, node))
                    stack.append((WHITE, node.left))
                else:
                    res.append(node.val)
        return res

    def inorderTraversal_morris1(self, root: TreeNode):
        '''
        莫里斯遍历1 此写法会改变树结构
        本方法中，我们使用一种新的数据结构：线索二叉树。方法如下：
            Step 1: 将当前节点current初始化为根节点
            Step 2: While current不为空，
            若current没有左子节点
                a. 将current添加到输出
                b. 进入右子树，亦即, current = current.right
            否则
                a. 在current的左子树中，令current成为最右侧节点的右子节点
                b. 进入左子树，亦即，current = current.left
        :param root:
        :return:
        '''
        res = []
        cur = root
        # tmp_root = root
        while cur is not None:
            if cur.left is None:  # or (cur.right is not None and cur.right == tmp_root):
                res.append(cur.val)
                # tmp_root = cur
                cur = cur.right

            else:
                # 缓存左节点指针
                tmp_cur = cur.left
                tmp_right = cur.left
                # 当前节点左节点置空
                cur.left = None
                # 找到左节点的最右节点
                while tmp_right.right:
                    tmp_right = tmp_right.right
                # 当前节点变成最右节点的右节点
                tmp_right.right = cur
                # 左节点成主节点
                cur = tmp_cur
        return res

    def inorderTraversal_morris(self, root: TreeNode):
        '''
        莫里斯遍历2 此写法不会改变树结构
        :param root:
        :return:
        '''
        res = []
        cur = root
        while cur is not None:
            if cur.left is None:
                res.append(cur.val)
                cur = cur.right
            else:
                most_right = self.get_left_most_right(cur)
                if most_right.right == cur:
                    most_right.right = None
                    res.append(cur.val)
                    cur = cur.right
                else:
                    most_right.right = cur
                    cur = cur.left
        return res

    def get_left_most_right(self, root):
        node = root.left
        while node and node.right and node.right != root:
            node = node.right
        return node


if __name__ == '__main__':
    sc = Solution()
    data = [1, None, 2, 3, 4, 5, 6, 7, 8]
    # data = [3, 4, None, None, 2, None, 1]
    t = ltn.gen_tree(data)
    print(sc.inorderTraversal(t))
    print(ltn.print_tree(t))
    t1 = ltn.gen_tree(data)
    print(sc.inorderTraversal1(t1))
    print(ltn.print_tree(t1))
