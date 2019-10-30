#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/10/25 10:50
# @Software: PyCharm
# @File    : l1007_min_domino_rotations.py


class Solution:
    def __init__(self):
        '''
        在一排多米诺骨牌中，A[i] 和 B[i] 分别代表第 i 个多米诺骨牌的上半部分和下半部分。（一个多米诺是两个从 1 到 6 的数字同列平铺形成的 —— 该平铺的每一半上都有一个数字。）
我们可以旋转第 i 张多米诺，使得 A[i] 和 B[i] 的值交换。
返回能使 A 中所有值或者 B 中所有值都相同的最小旋转次数。
如果无法做到，返回 -1.
链接：https://leetcode-cn.com/problems/minimum-domino-rotations-for-equal-row
        '''
        self.dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        self.dicA = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        self.dicB = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        self.max = 0
        self.max_index = []

    def minDominoRotations1(self, A, B) -> int:
        for a, b in zip(A, B):
            self.dicA[a] += 1
            self.dicB[b] += 1

            self.dic[a] += 1
            self.setMax(self.dic[a], a)
            if a != b:
                self.dic[b] += 1
                self.setMax(self.dic[b], b)
        if self.max < len(A):
            return -1
        else:
            res = len(A) - max(self.dicA[self.max_index[0]], self.dicB[self.max_index[0]])
        return res

    def setMax(self, cur_count, cur_key):
        if cur_count >= self.max:
            self.max = cur_count
            self.max_index = [cur_key]
        # elif cur_count == self.max:
        #     self.max_index.append(cur_key)

    def minDominoRotations2(self, A, B) -> int:
        if len(A) != len(B):
            return -1
        if not A:
            return 0

        min_rotations = min(self.check_val(A[0], A, B),
                            self.check_val(B[0], A, B))

        if min_rotations == float('inf'):
            return -1
        return min_rotations

    def check_val(self, val, A, B):
        i = 0
        rot_a, rot_b = 0, 0
        while i < len(A):
            if A[i] != val and B[i] != val:
                return float('inf')

            if B[i] != val:  # B[i] != val
                rot_b += 1
            elif A[i] != val:
                rot_a += 1
            i += 1
        if i == len(A):
            return min(rot_a, rot_b)
        return float('inf')

    def minDominoRotations(self, A, B) -> int:
        for x in range(1, 7):
            if all(x == a or x == b for a, b in zip(A, B)):
                return min(len(A) - A.count(x), len(B) - B.count(x))
        return -1


if __name__ == '__main__':
    s = Solution()
    # A = [3, 5, 1, 2, 3]
    # B = [3, 6, 3, 3, 4]
    # A = [1, 5, 2, 4, 2, 2]
    # B = [2, 2, 6, 2, 3, 2]
    A = [2, 4, 3, 2]
    B = [3, 2, 2, 1]
    res = s.minDominoRotations1(A, B)
    print(res)
