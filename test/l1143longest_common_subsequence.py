#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/11/4 16:49
# @Software: PyCharm
# @File    : l1143longest_common_subsequence.py


class Solution:
    def __init__(self):
        """
        “子串”指的是“子字符串(sub-string)”要求字符是相连的。子序列(subsequent)不要求字符相邻，只要位置在原字符串中的先后顺序一致即可。这些可参见wiki
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列。
一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
若这两个字符串没有公共子序列，则返回 0。
示例 1:
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3。
链接：https://leetcode-cn.com/problems/longest-common-subsequence
        """
        pass

    def longestCommonSubstring(self, s: str, s2: str) -> int:
        '''
        子串(连续)
        :param s:
        :param s2:
        :return:
        '''
        if len(s) == 0 or len(s2) == 0:
            return ''
        c1, c2, max_c = len(s), len(s2), 0
        dp = [[0 for i in range(c2)] for j in range(c1)]
        for i, val_i in enumerate(s):
            for j, val_j in enumerate(s2):
                if val_i == val_j:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    max_c = max(dp[i][j], max_c)
        for i in dp:
            print(i)
        return max_c

    def longestCommonSubsequence(self, s, s2):
        '''
        子序列（不用连续）
        :param s:abcdefgh
        :param s2:aeadf
        :return:
        '''
        c1, c2, max_c = len(s), len(s2), 0
        dp = [[0 for i in range(c2 + 1)] for j in range(c1 + 1)]
        for i, val_i in enumerate(s, start=1):
            for j, val_j in enumerate(s2, start=1):
                if val_i == val_j:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    # if i == 0 or j == 0:
                    #     dp[i][j] = 1
                    # else:
                    #     dp[i][j] = dp[i - 1][j - 1] + 1
                    # max_c = max(dp[i][j], max_c)
                else:
                    dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
                    # if i > 0 and j > 0:
                    #     dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
                    # elif j > 0:
                    #     dp[i][j] = dp[i][j - 1]
                    # elif i > 0:
                    #     dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]


if __name__ == '__main__':
    '''
    "bsbininm"
    "jmjkbkjkv"
    
    "pmjghexybyrgzczy"
    "hafcdqbgncrcbihkd"
    
     s1 = 'abcde'
    s2 = 'abadfe'
    
     a b c d e
   a 1 1 1 1 1   
   b 1 2 2 2 2 
   a 1 2 2 2 2
   c 1 2 
   d 1 2 2 3 3
   f 1 2 2 3 3
   e 1 2 2 3 4
'''
    sc = Solution()
    s2 = "jmjkbkjkv"
    s1 = "bsbininm"
    # s2 = "pmjghexybyrgzczy"
    # s1 = "hafcdqbgncrcbihkd"
    # s1 = 'abcde'
    # s2 = 'adce'

    print(sc.longestCommonSubsequence(s1, s2))
