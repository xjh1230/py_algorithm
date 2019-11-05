#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/11/4 15:17
# @Software: PyCharm
# @File    : l5_longest_palindrome.py


class Solution:
    def __init__(self):
        """
        给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：
输入: "cbbd"
输出: "bb"
https://leetcode-cn.com/problems/longest-palindromic-substring
        """
        pass

    def longestPalindrome1(self, s: str) -> str:
        '''
        中心扩散
        :param s:
        :return:
        '''
        i = l = r1 = r2 = maxc = 0
        count = len(s)
        dic = {}
        if count < 2:
            return s
        while i < count - 1:
            if s[i] == s[i + 1]:
                l = i
                r1 = i + 1
                tmp = ''
                while l > -1 and r1 < count:
                    if s[l] == s[r1]:
                        tmp = s[l] + tmp + s[r1]
                        l -= 1
                        r1 += 1
                    else:
                        break
                if len(tmp) > maxc:
                    maxc = len(tmp)
                    dic[maxc] = tmp
            l = i - 1
            r2 = i + 1
            tmp = s[i]
            while l > -1 and r2 < count:
                if s[l] == s[r2]:
                    tmp = s[l] + tmp + s[r2]
                    l -= 1
                    r2 += 1
                else:
                    break
            if len(tmp) > maxc:
                maxc = len(tmp)
                dic[maxc] = tmp
            i += 1
            if (count - i + 1) * 2 < maxc:
                break
        return dic[maxc]

    def longestPalindrome(self, s):
        '''
        马拉车算法(中心扩展算法的补充，中间填充特殊字符串，就不会判断 aa 和 aba的问题)
        :param s:
        :return:
        '''
        if len(s) <= 1:
            return s
        maxc, dic = 1, {1: [s[0]]}
        s = '^' + ''.join(i + '#' for i in s)
        s = s[:-1] + '$'
        start, end = 0, len(s)

        while start < end:
            left = start - 1
            right = start + 1
            tmp = s[start]
            while left > 0 and right < end:
                if s[left] == s[right]:
                    tmp = s[left] + tmp + s[right]
                    left -= 1
                    right += 1
                else:
                    break
            if len(tmp) >= maxc:
                maxc = len(tmp)
                if maxc in dic:
                    dic[maxc].append(tmp)
                else:
                    dic[maxc] = [tmp]
            start += 1
            if (end - start + 1) * 2 < maxc:
                break
        res, max_res = '', 0
        for i in dic[maxc]:
            tmp = i.replace('#', '').replace('$', '')
            if len(tmp) > max_res:
                res = tmp
                max_res = len(tmp)
        return res

    def longestCommonSubstring(self, s, s2):
        '''
        最长公共子串
        :param s:
        :return:
        '''
        if len(s) < len(s2):
            s, s2 = s2, s
        max_c, max_index, c1, c2 = 1, 0, len(s), len(s2)
        dp = [[0] * c1] * c2
        for i, tmp1 in enumerate(s2):
            for j, tmp2 in enumerate(s):
                if tmp1 == tmp2:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                if max_c < dp[i][j]:
                    max_index = i
                    max_c = dp[i][j]
        print(max_c, max_index, s[max_index + 1 - max_c:max_index + 1] + '*', dp)


if __name__ == '__main__':
    sc = Solution()
    s = '123'
    s2 = '1234'
    print(sc.longestCommonSubstring(s, s2))
