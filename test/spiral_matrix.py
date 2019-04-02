# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 15:41
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : spiral_matrix.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/spiral-matrix/
        给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

        示例 1:

        输入:
        [
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]
        输出: [1,2,3,6,9,8,7,4,5]
        '''
        pass

    def spiralOrder1(self, matrix):
        m = len(matrix)
        if m < 1:
            return []
        n = len(matrix[0])
        if n < 1:
            return []
        ret = [0] * (m * n)
        count, row, col = 0, 0, 0
        min_row, max_row, min_col, max_col = 0, m - 1, 0, n - 1
        print(m, n)
        while count < m * n:
            print(count, '---', row, col)
            ret[count] = matrix[row][col]
            if count == 13:
                i = 0
            if row == min_row:
                if col < max_col:
                    col += 1
                else:
                    row += 1
            elif row == max_row:
                if col > min_col:
                    col -= 1
                else:
                    row -= 1
            else:
                if min_col == max_col:
                    if n % 2 == 1:
                        row += 1
                    else:
                        row -= 1
                else:
                    if col == min_col:
                        row -= 1
                        if row == min_row:
                            min_col += 1
                            max_row -= 1
                    elif col == max_col:
                        row += 1
                        if row == max_row:
                            max_col -= 1
                            min_row += 1
            count += 1
        return ret

    def spiralOrder(self, matrix):
        res = []
        m = len(matrix)
        if m > 0:
            n = len(matrix[0])
            self.write_line(matrix, res, 0, 0, 0, m, n)
        return res

    def write_line(self, matrix, res, start_row, start_col, op, row_count, col_count):
        if op == 0:  # 左
            if start_col < col_count:
                for i in range(start_col, col_count):
                    res.append(matrix[start_row][i])
                self.write_line(matrix, res, start_row + 1, start_col, 1, row_count, col_count - 1)
        elif op == 1:  # 下
            if start_row < row_count:
                for i in range(start_row, row_count):
                    res.append(matrix[i][col_count])
                self.write_line(matrix, res, start_row, start_col, 2, row_count - 1, col_count)
        elif op == 2:  # 右
            if start_col < col_count:
                for i in range(col_count - 1, start_col - 1, -1):
                    res.append(matrix[row_count][i])
                self.write_line(matrix, res, start_row, start_col, 3, row_count, col_count)
        else:  # 上
            if start_row < row_count:
                for i in range(row_count - 1, start_row - 1, -1):
                    res.append(matrix[i][start_col])
                self.write_line(matrix, res, start_row, start_col + 1, 0, row_count, col_count)


if __name__ == '__main__':
    s = Solution()
    m = [[j for j in range(4)] for i in range(2)]
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
    # m = [
    #     [1, 2, 3, 4],
    #     [5, 6, 7, 8],
    #     [9, 10, 11, 12]
    # ]
    # m = [[7], [9], [6]]

    # m = [[2, 3, 4],
    #      [5, 6, 7],
    #      [8, 9, 10],
    #      [11, 12, 13],
    #      [14, 15, 16]]

    # m = [[], [], []]

    # m = [[1, 2, 3, 4],
    #      [5, 6, 7, 8],
    #      [9, 10, 11, 12],
    #      [13, 14, 15, 16]]
    # print(m)
    print(s.spiralOrder(m))
