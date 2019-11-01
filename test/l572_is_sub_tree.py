#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/11/1 15:00
# @Software: PyCharm
# @File    : l572_is_sub_tree.py


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        '''
        给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

示例 1:
给定的树 s:

     3
    / \
   4   5
  / \
 1   2
给定的树 t：

   4
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。
链接：https://leetcode-cn.com/problems/subtree-of-another-tree


[1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,2]
[1,null,1,null,1,null,1,null,1,null,1,2]

[1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,2]
[1,None,1,None,1,None,1,None,1,None,1,2]
                    1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,2
        1             None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,2
          1                  None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,2
            1                       None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,2
              1                            None,1,None,1,None,1,None,1,None,1,None,1,None,1,2
                1                                 None,1,None,1,None,1,None,1,None,1,None,1,2
                  1                                      None,1,None,1,None,1,None,1,None,1,2
                    1                                           None,1,None,1,None,1,None,1,2
                      1                                                None,1,None,1,None,1,2
                        1                                                     None,1,None,1,2
                          1                                                          None,1,2
                         2
                         1,None,1,None,1,None,1,None,1,None,1,2
                    None,1,None,1,None,1,None,1,None,1,None,1,2
        '''
        pass

    def isSubtree1(self, s: TreeNode, t: TreeNode) -> bool:
        return self.isSamtree(s, t) or (s.left is not None and self.isSubtree(s.left, t)) or (
                s.right is not None and self.isSubtree(s.right, t))

    def isSamtree(self, s, t):
        if s is None:
            return t is None
        if t is None:
            return s is None
        return s.val == t.val and self.isSamtree(s.left, t.left) and self.isSamtree(s.right, t.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def inorder(root):
            if not root:
                return '#'
            return '*' + str(root.val) + inorder(root.left) + inorder(root.right)  # '*' +

        ss = inorder(s)
        tt = inorder(t)
        print(ss, tt)
        return tt in ss


def gen_tree(li):
    if len(li) == 0:
        return None
    t = TreeNode(li[0])
    li_tree = [t]
    cur = li_tree.pop(0)
    set_left = False
    set_right = False
    for i in li[1:]:
        if not set_left:
            cur.left = gen_tree_node(i, li_tree)
            set_left = True
        elif not set_right:
            cur.right = gen_tree_node(i, li_tree)
            set_right = True
        else:
            cur = li_tree.pop(0)
            cur.left = gen_tree_node(i, li_tree)
            set_left = True
            set_right = False
    return t


def gen_tree_node(s, li):
    if s is None:
        return s
    else:
        t = TreeNode(s)
        li.append(t)
        return t


if __name__ == '__main__':
    s = Solution()
    p = [1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, 2]
    c = [1, None, 1, None, 1, None, 1, None, 1, None, 1, 2]
    p = [1, 2, 3]
    c = [2, 3]
    p_t = gen_tree(p)
    c_t = gen_tree(c)
    print(s.isSubtree(p_t, c_t))
