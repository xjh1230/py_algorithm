#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/11/9 13:10
# @Software: PyCharm
# @File    : l994_oranges_rotting.py


class Solution:
    def __init__(self):
        """
        在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

链接：https://leetcode-cn.com/problems/rotting-oranges
        """
        pass

    def orangesRotting(self, grid) -> int:
        res = 0
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        count_y, count_x = len(grid), len(grid[0])
        li_bad, li_good, empty, good, bad, total = {}, {}, 0, 0, 0, count_y * count_x
        for row in range(count_y):
            for col in range(count_x):
                if grid[row][col] == 0:
                    empty += 1
                if grid[row][col] == 1:
                    left = 0 if col == 0 else grid[row][col - 1]
                    right = 0 if col == count_x - 1 else grid[row][col + 1]
                    top = 0 if row == 0 else grid[row - 1][col]
                    down = 0 if row == count_y - 1 else grid[row + 1][col]
                    if left == right == top == down == 0:
                        return -1
                    else:
                        li_good[(row, col)] = 0
                    good += 1
                elif grid[row][col] == 2:
                    li_bad[(row, col)] = 0
                    bad += 1
        if bad == 0 and good > 0:
            return -1
        if good + empty == total:
            return 0
        while li_good and res < total:
            li_tmp = {}
            for cur in li_bad.keys():
                left = (cur[0], cur[1] - 1)
                self.check_good(li_good, li_tmp, left)
                right = (cur[0], cur[1] + 1)
                self.check_good(li_good, li_tmp, right)
                top = (cur[0] - 1, cur[1])
                self.check_good(li_good, li_tmp, top)
                down = (cur[0] + 1, cur[1])
                self.check_good(li_good, li_tmp, down)
            li_bad = li_tmp
            res += 1
        return res if res < total else -1

    def check_good(self, li_good, li_tmp, cur):
        if cur in li_good:
            del li_good[cur]
            li_tmp[cur] = 0

    def orangesRotting1(self, grid):
        x, y, time = len(grid), len(grid[0]), 0
        locs, stack = [[-1, 0], [0, -1], [0, 1], [1, 0]], []
        for i in range(x):
            for j in range(y):
                if grid[i][j] == 2:
                    stack.append((i, j, 0))
        while stack:
            i, j, time = stack.pop(0)
            for loc in locs:
                loc_i, loc_j = i + loc[0], j + loc[1]
                if 0 <= loc_i < x and 0 <= loc_j < y and grid[loc_i][loc_j] == 1:
                    grid[loc_i][loc_j] = 2
                    stack.append((loc_i, loc_j, time + 1))
        for g in grid:
            if 1 in g:
                return -1
        return time


if __name__ == '__main__':
    sc = Solution()
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    # grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    # grid = [[0, 2]]
    # grid = [[1, 1, 1]]
    # grid = [[0, 0, 0]]
    # grid = [[2, 2, 2]]
    # grid = [[2], [2], [1], [0], [1], [1]]
    print(sc.orangesRotting(grid))
