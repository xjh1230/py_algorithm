# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 15:22
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : convert_bst.py
# @Software: PyCharm

from functools import reduce


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

    def convertBST(self, root):
        count = len(root)
        # start_index = int(bin(count)[:3] + (len(bin(count)) - 3) * '0', 2)
        li = self.get_node(1, count)
        li = [i - 1 for i in li]
        result = [0] * count

        def get_sum(x, y):
            if x == -1:
                return root[y]
            else:
                return x + root[y]

        for i, v in enumerate(result):
            index = li.index(i)
            result[i] = reduce(get_sum, [-1] + li[index:])
            # print(index, li[index:], i, result[i])

        return result

    def get_node(self, node, max_index):
        '''
        :param node:  1 为起点
        :param max_index:
        :return:
        '''
        li = []
        li += self.get_left(node, max_index)
        li.append(node)
        li += self.get_right(node, max_index)
        # print(li)
        return li

    def get_left(self, node, max_index):
        if node >= max_index:
            return []
        left = node * 2
        left_max = self.get_max(left)
        if left_max >= max_index:
            if left <= max_index:
                return [left]
            return []
        else:
            return self.get_node(left, max_index)

    def get_right(self, node, max_index):
        if node >= max_index:
            return []
        right = (node * 2) + 1
        right_max = self.get_max(right)
        if right_max >= max_index:
            if right <= max_index:
                return [right]
            return []
        else:
            return self.get_node(right, max_index)

    def get_max(self, cur):
        return int(bin(cur)[:3] + (len(bin(cur)) - 3) * '1', 2)


if __name__ == '__main__':
    s = Solution()
    li = [8,4,12,2,6,10,14,1,3,5,7,9]
    # [7, 4, 11, 2, 5, 9, 13]    [40,49,24,51,45,33,13]
    #  [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]  [92,114,54,119,105,75,29,120,117,110,99,84,65,42,15]
    # [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9]  [53, 75, 26, 80, 66, 36, 14, 81, 78, 71, 60, 45]
    res = s.convertBST(li)
    # res = s.get_node(1, 4)
    print(res)
