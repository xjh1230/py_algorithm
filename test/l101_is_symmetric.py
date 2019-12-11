#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/11/25 14:52
# @Software: PyCharm
# @File    : l101_is_symmetric.py

from data_structure.leecode_tree_node import TreeNode
from data_structure.leecode_tree_node import gen_tree


class Solution:
    def __init__(self):
        """
        """
        pass

    def isSymmetric1(self, t: TreeNode) -> bool:
        if not t:
            return True

        def isSame(left: TreeNode, right: TreeNode):
            if left is None or right is None:
                return left is None and right is None
            elif left.val == right.val:
                return isSame(left.left, right.right) and isSame(left.right, right.left)
            else:
                return False

        return isSame(t.left, t.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = [root.left, root.right]
        while queue:
            left = queue.pop()
            right = queue.pop()
            if right is None or left is None:
                if left is None and right is None:
                    continue
                else:
                    return False
            elif right.val == left.val:
                queue.append(left.left)
                queue.append(right.right)
                queue.append(left.right)
                queue.append(right.left)
            else:
                return False
        return True


if __name__ == '__main__':
    sc = Solution()
    li = [2, 3, 3, 4, 5, None, 4]
    t = gen_tree(li)
    print(sc.isSymmetric(t))
