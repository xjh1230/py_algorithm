#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/11/6 15:43
# @Software: PyCharm
# @File    : l187_find_repeated_dna_sequences.py


class Solution:
    def __init__(self):
        """
        所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。
编写一个函数来查找 DNA 分子中所有出现超过一次的 10 个字母长的序列（子串）。
示例：
输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC", "CCCCCAAAAA"]

https://leetcode-cn.com/problems/repeated-dna-sequences
        """
        pass

    def findRepeatedDnaSequences1(self, s):
        dic = {}
        if len(s) < 11:
            return ''
        li = []
        for i in range(10, len(s) + 1):
            tmp = s[i - 10:i]
            c = dic.get(tmp, 0)
            if c == 1:
                li.append(tmp)
            dic[tmp] = c + 1
        return li

    def findRepeatedDnaSequences2(self, s):
        visited = set()
        res = set()
        for i in range(0, len(s) - 9):
            tmp = s[i:i + 10]
            if tmp in visited:
                res.add(tmp)
            visited.add(tmp)
        return list(res)

    def findRepeatedDnaSequences(self, s):
        exit_s = [False] * (1 << 20)
        add_s = [False] * (1 << 20)
        li = []
        k = (1 << 18) - 1
        key = 0
        for i in range(0, len(s)):
            key <<= 2
            key += self.getVal(s[i])
            if i > 8:
                if exit_s[key]:
                    if not add_s[key]:
                        li.append(s[i - 9:i + 1])
                        add_s[key] = True
                else:
                    exit_s[key] = True
            key &= k
        return li

    def getVal(self, c):
        if c == 'A':
            v = 0
        elif c == 'C':
            v = 1
        elif c == 'G':
            v = 2
        elif c == 'T':
            v = 3
        else:
            raise Exception
        return v


if __name__ == '__main__':
    sc = Solution()
    s = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
    print(sc.findRepeatedDnaSequences(s))
