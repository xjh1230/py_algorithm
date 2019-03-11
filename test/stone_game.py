# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 10:14
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : stone_game.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/stone-game/
        亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。

游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。

亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。

假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。
        '''
        self.li = []
        pass

    def stoneGame(self, piles):
        self.li = piles
        N = len(piles)
        result = []
        for i in range(N):
            tmp = [0 for i in range(N)]
            result.append(tmp)
        for size in range(1, N + 1):
            i = 0
            while i + size < N:
                j = i + size - 1
                parity = (i + j + N) % 2
                if parity == 1:
                    result[i][j] = max(piles[i] + result[i + 1][j], piles[j] + result[i][j - 1])
                else:
                    result[i][j] = min(-piles[i] + result[i + 1][j], -piles[j] + result[i][j - 1])
                i += 1

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.stoneGame([5, 12, 33, 11, 5, 5]))


def fib(n):
    if n <= 0:
        return n
    li = [-1 for i in range(n + 1)]
    li[0] = 0
    li[1] = 1
    for i in range(2, n + 1):
        li[i] = li[i - 1] + li[i - 2]
    return li[n]


