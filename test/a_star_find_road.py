#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2020/5/13 11:26
# @Software: PyCharm
# @File    : a_star_find_road.py


STEP = 10
OBLIQUE = 14


class Point:
    def __init__(self, x, y):
        '''
        F = G + H
        G = 从起点A，沿着产生的路径，移动到网格上指定方格的移动耗费。
H = 从网格上那个方格移动到终点B的预估移动耗费。这经常被称为启发式的，可能会让你有点迷惑。这样叫的原因是因为它只是个猜测。我们没办法事先知道路径的长度，
因为路上可能存在各种障碍(墙，水，等等)。虽然本文只提供了一种计算H的方法，但是你可以在网上找到很多其他的方法。
        :param x:
        :param y:
        '''
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.parent = None

    def calc_f(self):
        self.f = self.g + self.h


def find_point(li, x, y):
    for tmp in li:
        if tmp.x == x and tmp.y == y:
            return tmp
    return None


class a_star_find_road:
    def __init__(self, maze):
        """
        """
        self.open_list = []
        self.close_list = []
        self.maze = maze
        self.count = 0

    def find_min(self):
        def take_f(point):
            return point.f

        if len(self.open_list) > 0:
            self.open_list.sort(key=take_f, reverse=True)
            return self.open_list.pop()
        else:
            return None

    def _can_reach(self, x, y):
        return self.maze[x][y] == 0

    def can_reach(self, point, x, y, is_ignore_corner):
        if not self._can_reach(x, y) or find_point(self.close_list, x, y):
            return False
        else:
            if abs(x - point.x) + abs(y - point.y) == 1:  # x,y是point上下左右
                return True
            else:
                if self._can_reach(abs(x - 1), y) and self._can_reach(x, abs(y - 1)):  # x,y是point的斜方向
                    return True
                else:
                    return is_ignore_corner

    def find_surround(self, point, is_ignore_corner):
        res = []
        x = point.x - 1
        while x <= point.x + 1:
            y = point.y - 1
            while y <= point.y + 1:
                if self.can_reach(point, x, y, is_ignore_corner):
                    p = Point(x, y)
                    p.parent = point
                    res.append(p)
                y += 1
            x += 1
        return res

    def calc_h(self, end, point):
        return (abs(end.x - point.x) + abs(end.y - point.y)) * STEP

    def calc_g(self, start, point):
        g = STEP if abs(start.x - point.x) + abs(start.y - point.y) == 1 else OBLIQUE
        parent_g = 0 if point.parent is None else point.parent.g
        return g + parent_g

    def found_point(self, current, point):
        g = self.calc_g(current, point)
        if g <= point.g:
            point.parent = current
            point.g = g
            point.calc_f()

    def no_found_point(self, current, end, point):
        point.parent = current
        point.g = self.calc_g(current, point)
        point.h = self.calc_h(end, point)
        point.calc_f()
        self.open_list.append(point)

    def find_path(self, start, end, is_ignore_corner=True):
        self.open_list.append(start)
        while len(self.open_list) > 0:
            current = self.find_min()
            self.close_list.append(current)
            surround = self.find_surround(current, is_ignore_corner)
            for point in surround:
                self.count += 1
                if find_point(self.open_list, point.x, point.y):  # 在开始列表 计算G值, 如果比原来的大, 就什么都不做, 否则设置它的父节点为当前点,并更新G和F
                    self.found_point(current, point)
                else:  # 如果它们不在开始列表里, 就加入, 并设置父节点,并计算GHF
                    self.no_found_point(current, end, point)

            if find_point(self.open_list, end.x, end.y):
                return find_point(self.open_list, end.x, end.y)
        return find_point(self.open_list, end.x, end.y)


if __name__ == '__main__':
    maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
            [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    start = Point(6,3)
    end = Point(1, 7)
    s = a_star_find_road(maze)
    p = s.find_path(start, end)
    print(s.count)
    while p:
        print(p.x, p.y, p.f, p.g, p.h)
        p = p.parent
    p1 = find_point(s.open_list, 2, 2)
    p2 = find_point(s.close_list, 2, 2)
    p1 = p2
    # print(start.f, start.g, start.h, p.f, p.g, p.h)
