# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 9:39
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : perfect_square.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        '''
        给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。
        你需要让组成和的完全平方数的个数最少。
        https://leetcode-cn.com/problems/perfect-squares/
        '''
        pass

    def numSquares1(self, n: int) -> int:
        '''
        四平方公式计算
        :param n:
        :return:
        '''
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        a = 0
        while a * a <= n:
            b = (n - a * a) ** 0.5
            if a ** 2 + int(b) ** 2 == n:
                if a == 0 or b == 0:
                    return 1
                else:
                    return 2
            a += 1
        return 3

    def numSquares(self, n: int) -> int:
        '''
        bfs(广度优先处理)
        :param n:
        :return:
        '''
        level = 1
        queue = [n]
        while True:
            li = []
            while queue:
                tmp = queue.pop()
                for i in range(1, tmp + 1):
                    sub = tmp - i ** 2
                    if sub == 0:
                        return level
                    elif sub > 0:
                        li.append(sub)
                    else:
                        break
            queue = li
            level += 1
        return level


if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(12))
