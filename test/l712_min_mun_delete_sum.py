#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2021/3/22 16:16
# @Software: PyCharm
# @File    : l712_min_mun_delete_sum.py

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        '''
        动态规划的变异用法
        :param s1:
        :param s2:
        :return:
        '''
        sum_i = 0
        for c in s1:
            sum_i += ord(c)
        for c in s2:
            sum_i += ord(c)
        dp = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + ord(s1[i])
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return sum_i - dp[len(s1)][len(s2)] * 2


if __name__ == '__main__':
    s = Solution()
    s1 = 'sea'
    s2 = 'eat'
    print(s.minimumDeleteSum(s1, s2))
