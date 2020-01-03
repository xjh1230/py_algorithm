#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2020/1/2 17:55
# @Software: PyCharm
# @File    : l322_coin_change.py

class Solution:
    def __init__(self):
        """
        """

    def coinChange1(self, coins, amount: int) -> int:
        dic = {}
        min_c = min(coins)
        for c in coins:
            dic[c] = 1
        if amount == 0:
            return 0

        def getCoin(amount):
            if amount in dic:
                return dic[amount]
            if amount < min_c:
                dic[amount] = -1
                return -1
            else:
                tmp = [getCoin(amount - i) for i in coins]
                tmp = [i + 1 for i in tmp if i != -1]
                if tmp:
                    dic[amount] = min(tmp)
                else:
                    dic[amount] = -1
                return dic[amount]

        return getCoin(amount)

    def coinChange2(self, coins, amount: int) -> int:
        if amount == 0:
            return 0
        res = [0 for i in range(amount + 1)]
        for i in range(1, amount + 1):
            tmp = float('inf')
            for c in coins:
                if i - c >= 0:
                    tmp = min(tmp, res[i - c] + 1)
            res[i] = tmp
        if res[amount] == float('inf'):
            return -1
        return res[amount]

    def coinChange(self, coins, amount: int) -> int:
        self.minCount = float('inf')
        coins.sort()
        self.dfs(coins, amount, 0, len(coins) - 1)
        return -1 if self.minCount == float('inf') else int(self.minCount)

    def dfs(self, coins, amount, count, index):
        if index < 0 or count + amount // coins[index] >= self.minCount:
            return
        if amount % coins[index] == 0:
            self.minCount = min(self.minCount, count + amount // coins[index])
        else:
            for i in range(amount // coins[index], -1, -1):
                self.dfs(coins, amount - i * coins[index], count + i, index - 1)


if __name__ == '__main__':
    s = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(s.coinChange(coins, amount))
    # coins = [1]
    # amount = 0
    # print(s.coinChange(coins, amount))
