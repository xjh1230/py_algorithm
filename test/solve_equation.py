# -*- coding: utf-8 -*-
# @Time    : 2019/1/30 12:06
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : solve_equation.py
# @Software: PyCharm

import re
import math


class Solution:
    def solveEquation(self, equation):
        """
        求解一个给定的方程，将x以字符串"x=#value"的形式返回。该方程仅包含'+'，' - '操作，变量 x 和其对应系数。

如果方程没有解，请返回“No solution”。

如果方程有无限解，则返回“Infinite solutions”。

如果方程中只有一个解，要保证返回值 x 是一个整数。
        :type equation: str
        :rtype: str
        """
        result = ''
        li = equation.split('=')
        li_left = li[0]
        li_right = li[1]
        x_patt = re.compile('([+|-]*[\d]*)x')
        d_patt = re.compile('([+|-]*[\d]+)')
        x_left = x_patt.findall(li_left)
        tmp = re.sub(x_patt, '', li_left)
        d_left = d_patt.findall(tmp)
        # print(tmp, li_left, equation)
        x_right = x_patt.findall(li_right)
        tmp = re.sub(x_patt, '', li_right)
        d_right = d_patt.findall(tmp)
        # print(x_left, x_right, d_left, d_right, equation)
        # print(x_left, self.change(x_left), self.sum(self.change(x_left)))
        # print(x_right, self.change(x_right), self.sum(self.change(x_right)))
        # print(d_left, self.change(d_left), self.sum(self.change(d_left)))
        # print(d_right, self.change(d_right), self.sum(self.change(d_right)))
        x_total = self.sum(self.change(x_left)) - self.sum(self.change(x_right))
        d_total = self.sum(self.change(d_right)) - self.sum(self.change(d_left))
        # print(x_total, d_total, equation)
        if x_total == 0:
            if d_total == 0:
                result = 'Infinite solutions'
            else:
                result = 'No solution'
        else:
            if d_total == 0:
                result = 'x=0'
            else:
                result = 'x=' + str(round(d_total / x_total))
        print(equation)
        return result

    def change(self, li):
        result = []
        for i in li:
            if i == '' or i == '+':
                i = 1
            elif i == '-':
                i = -1
            result.append(int(i))
        return result

    def sum(self, li):
        result = 0
        for i in li:
            result += i
        return result

    def test(self):
        print(self.solveEquation('1+x+5+2x-4-3x+5-6=4x+3x+5'))
        print(self.solveEquation('x+5-3+x=6+x-2'))
        print(self.solveEquation('x=x'))
        print(self.solveEquation('2x=x'))
        print(self.solveEquation('x=x+2'))


if __name__ == '__main__':
    s = Solution()
    s.test()
