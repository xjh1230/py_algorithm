#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2020/11/11 14:46
# @Software: PyCharm
# @File    : l79word_search.py

class Solution:
    def __init__(self):
        '''
        今天天气真不错
        '''
        pass

    def exist(self, board, word):
        def find(i, j, cur):
            if i >= row or i < 0 or j >= col or j < 0: return False
            letter = board[i][j]

            if letter != word[cur]: return False
            if cur == len(word) - 1: return True
            board[i][j] = None
            next = cur + 1
            res = find(i - 1, j, next) or find(i + 1, j, next) or find(i, j - 1, next) or find(i, j + 1, next)
            board[i][j] = letter
            return res

        row = len(board)
        if row < 1: return False
        if len(word) < 1: return True
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                res = find(i, j, 0)
                if res:
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    board = [["a"]]
    word = "ABCB"
    word = "c"
    res = s.exist(board, word)
    print(res)
