# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 11:44
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : all_possible_fbt.py
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from data_structure.tree_node import TreeNode


class Solution:
    def __init__(self):
        '''
        满二叉树是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。

返回包含 N 个结点的所有可能满二叉树的列表。 答案的每个元素都是一个可能树的根结点。

答案中每个树的每个结点都必须有 node.val=0。

你可以按任何顺序返回树的最终列表。

示例：
输入：7
输出：[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-possible-full-binary-trees
        '''

        self.cache = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N: int):
        if N in self.cache:
            return self.cache[N]
        tree = []
        for i in range(1, N, 2):
            for l in self.allPossibleFBT(i):
                for r in self.allPossibleFBT(N - i - 1):
                    node = TreeNode(0)
                    node.left = l
                    node.right = r
                    tree.append(node)
        self.cache[N] = tree
        return self.cache[N]


if __name__ == '__main__':
    s = Solution()
    N = 7
    li = s.allPossibleFBT(N)
    for n in li:
        print(TreeNode.print_tree(n))
