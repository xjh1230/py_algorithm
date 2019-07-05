# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 15:28
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : coin_change_II.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/coin-change-2/
        给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
        示例 1:

        输入: amount = 5, coins = [1, 2, 5]
        输出: 4
        解释: 有四种方式可以凑成总金额:
        5=5
        5=2+2+1
        5=2+1+1+1
        5=1+1+1+1+1
        '''

    def change1(self, amount, coins) -> int:
        '''
        思路对，超时
        :param amount:
        :param coins:
        :return:
        '''
        if amount == 0:
            return 1
        coins.sort(reverse=True)

        def get_count(num, index, len):
            if index == len:
                return 0
            elif num < 0:
                return 0
            elif num < coins[index]:
                return get_count(num, index + 1, len)
            elif num == coins[index]:
                return 1 + get_count(num, index + 1, len)
            else:
                li = []
                for i in range(index, len):
                    li.append(get_count(num - coins[i], i, len))
                return sum(li)

        result = get_count(amount, 0, len(coins))
        return result

    def change(self, amount, coins):
        if amount == 0:
            return 1
        dic = {}
        for i in range(amount + 1):
            dic[i] = -1
        coins.sort(reverse=True)
        dic[coins[-1]] = 1
        dic[0] = 1

        def get_count(amount):
            if amount < 0:
                return -2
            if dic[amount] > -1:
                return dic[amount]
            elif dic[amount] == -2:
                return -2
            else:
                li = []
                for i in coins:
                    li.append(get_count(amount - i))
                li = [i for i in li if i > 0]
                if len(li) > 0:
                    dic[amount] = sum(li)
                else:
                    dic[amount] = -2
            return dic[amount]

        res = get_count(amount)
        print(dic)
        return res


if __name__ == '__main__':
    s = Solution()
    amount = 11
    li = [3, 5, 7, 8, 9, 10, 11]
    # res = s.change(amount, li)
    # print(res)
    res = s.change(amount, li)
    print(res)
