# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 13:08
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : spiral_matrix_ii.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/spiral-matrix-ii/
        给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
        示例:
        输入: 3
        输出:
        [
         [ 1, 2, 3 ],
         [ 8, 9, 4 ],
         [ 7, 6, 5 ]
        ]
        '''

    def generateMatrix(self, n: int):
        res = [[0 for i in range(n)] for i in range(n)]
        count = 1
        cur_row, cur_col, row, col, op = 0, 0, n, n, 0
        while True:
            if op == 0:  # 左
                for i in range(cur_col, col):
                    res[cur_row][i] = count
                    count += 1
                cur_row += 1
                op = 1
            elif op == 1:  # 下
                for i in range(cur_row, row):
                    res[i][col - 1] = count
                    count += 1
                col -= 1
                op = 2
            elif op == 2:  # 右
                for i in range(col - 1, cur_col - 1, -1):
                    res[row - 1][i] = count
                    count += 1
                row -= 1
                op = 3
            elif op == 3:  # 上
                for i in range(row - 1, cur_row - 1, -1):
                    res[i][cur_col] = count
                    count += 1
                cur_col += 1
                op = 0
            if count > n ** 2:
                break
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(5))
