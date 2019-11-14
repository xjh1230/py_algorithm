#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/11/13 10:39
# @Software: PyCharm
# @File    : l37_solve_sudoku.py

from random import shuffle


class Solution:
    def __init__(self):
        """
        编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。

链接：https://leetcode-cn.com/problems/sudoku-solver
        """
        self.count = 0

    def solveSudoku1(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def check(x, y, s):
            for i in range(9):
                if board[i][y] == s or board[x][i] == s:
                    return False
            for i in [0, 1, 2]:
                for j in [0, 1, 2]:
                    if board[x // 3 * 3 + i][y // 3 * 3 + j] == s:
                        return False
            return True

        def bt(cur):
            if cur == 81:
                return True
            x, y = cur // 9, cur % 9
            if board[x][y] != '.':
                return bt(cur + 1)
            for i in range(1, 10):
                s = str(i)
                if check(x, y, s):
                    board[x][y] = s
                    if bt(cur + 1):
                        return True
                    board[x][y] = '.'
            return False

        bt(0)

    def solveSudoku(self, board):
        rows, cols, blocks = [set([]) for _ in range(9)], [set([]) for _ in range(9)], [set([]) for _ in range(9)]
        emptys = {}
        alls = set([str(i) for i in range(1, 10)])
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    blocks[i // 3 * 3 + j // 3].add(board[i][j])
                else:
                    emptys[(i, j)] = board[i][j]
        while True:
            continued = False
            for (i, j) in emptys:
                val = (alls - rows[i]) & (alls - cols[j]) & (alls - blocks[i // 3 * 3 + j // 3])
                emptys[(i, j)] = val
                if len(val) == 1:
                    tmp = val.pop()
                    rows[i].add(tmp)
                    cols[j].add(tmp)
                    blocks[i // 3 * 3 + j // 3].add(tmp)
                    board[i][j] = tmp
                    continued = True
            if not continued:
                break
        emptys = {key: val for key, val in emptys.items() if len(val) > 0}
        if not emptys:
            return True
        empty_key = [k for k in emptys.keys()]
        empty_len = len(emptys)

        def bt(cur):
            if cur == empty_len:
                return True
            x, y = empty_key[cur]
            if board[x][y] == '.':
                maybe = (alls - rows[x]) & (alls - cols[y]) & (
                        alls - blocks[x // 3 * 3 + y // 3])
                if maybe:
                    for i in maybe:
                        board[x][y] = i
                        rows[x].add(i)
                        cols[y].add(i)
                        blocks[x // 3 * 3 + y // 3].add(i)
                        if bt(cur + 1):
                            return True
                        else:
                            rows[x].discard(i)
                            cols[y].discard(i)
                            blocks[x // 3 * 3 + y // 3].discard(i)
                            board[x][y] = '.'
                else:
                    return False
            else:
                return bt[cur + 1]

        bt(0)


class Solution1:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows, cols, blocks = [set([]) for _ in range(9)], [set([]) for _ in range(9)], [set([]) for _ in range(9)]
        alls = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

        emptys = {}

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    blocks[i // 3 * 3 + j // 3].add(board[i][j])
                else:
                    emptys[(i, j)] = board[i][j]
        while True:
            continued = False
            for (i, j) in emptys:
                val = (alls - rows[i]) & (alls - cols[j]) & (alls - blocks[i // 3 * 3 + j // 3])  # 交集
                emptys[(i, j)] = val
                if len(val) == 1:
                    tmp = val.pop()
                    rows[i].add(tmp)
                    cols[j].add(tmp)
                    blocks[i // 3 * 3 + j // 3].add(tmp)
                    board[i][j] = tmp
                    continued = True
            if not continued:
                break

        emptys = {key: val for key, val in emptys.items() if len(val) > 0}
        if not emptys:
            return

        empty_keys = [key for key in emptys.keys()]
        empty_len = len(empty_keys)

        def backtract(idx=0):
            k = empty_keys[idx]
            i, j = k
            for val in emptys[k]:
                if not (val in rows[i] or val in cols[j] or val in blocks[i // 3 * 3 + j // 3]):
                    if idx == empty_len - 1:  # 到了最后一个了，返回True
                        board[i][j] = val
                        return True
                    rows[i].add(val)
                    cols[j].add(val)
                    blocks[i // 3 * 3 + j // 3].add(val)
                    if not backtract(idx + 1):
                        rows[i].discard(val)
                        cols[j].discard(val)
                        blocks[i // 3 * 3 + j // 3].discard(val)
                    else:
                        board[i][j] = val
                        return True
            return False

        # backtract()


if __name__ == '__main__':
    sc = Solution()
    arr = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
           [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
           ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
           [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    # arr = [["5", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."],
    #        [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."],
    #        [".", ".", ".", ".", ".", ".", ".", ".", "1"], [".", ".", ".", ".", ".", ".", ".", ".", "."],
    #        [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."],
    #        [".", ".", ".", ".", ".", ".", ".", ".", "."]]
    sc.solveSudoku(arr)
    for li in arr:
        print(li)
