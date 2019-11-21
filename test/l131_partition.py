#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/11/15 16:05
# @Software: PyCharm
# @File    : l131_partition.py

import copy


class Solution:
    def __init__(self):
        """
        给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。
示例:
输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
链接：https://leetcode-cn.com/problems/palindrome-partitioning
        """
        self.dic = {}
        self.res_dic = {}

    def partition(self, s: str):
        if s in self.res_dic:
            return self.res_dic[s]
        if len(s) < 2:
            self.res_dic[s] = [[s]]
            return [[s]]
        tmp_li = self.partition(s[0:len(s) - 1])
        end_s = s[-1]
        res = []
        for li in tmp_li:
            cop = [i for i in li]
            cop.append(end_s)
            res.append(cop)
            cop = [i for i in li]
            last = cop[-1]
            if len(li) > 1 and self.check_hui(last + end_s):
                cop[-1] = last + end_s
                res.append(cop)
        if self.check_hui(s):
            res.append([s])
        for i in range(len(s) - 3):
            tmp_before = s[0:len(s) - 3 - i]
            tmp_end = s[len(s) - 3 - i:]
            if self.check_hui(tmp_end):
                tmp_li = self.partition(tmp_before)
                for li in tmp_li:
                    cop = copy.copy(li)
                    cop.append(tmp_end)
                    res.append(cop)
        dist = list(set([tuple(t) for t in res]))
        res = [list(v) for v in dist]
        self.res_dic[s] = res
        return res

    def check_hui(self, s):
        if s in self.dic:
            return self.dic[s]
        if len(s) == 1:
            self.dic[s] = True
            return True
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                self.dic[s] = False
                return False
        self.dic[s] = True
        return True


if __name__ == '__main__':
    sc = Solution()
    # print(sc.check_hui('abcba'))
    s = 'abcba'
    s = "danaranad"
    res = sc.partition(s)
    print(len(res))
    for i in res:
        print(i)
    li = [["d", "a", "n", "a", "r", "a", "n", "a", "d"], ["d", "a", "n", "a", "r", "ana", "d"],
          ["d", "a", "n", "ara", "n", "a", "d"], ["d", "a", "naran", "a", "d"], ["d", "ana", "r", "a", "n", "a", "d"],
          ["d", "ana", "r", "ana", "d"], ["d", "anarana", "d"], ["danaranad"]]
    print('1' * 30, len(li))
    for i in li:
        print(i)
