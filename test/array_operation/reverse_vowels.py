#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/12/26 16:48
# @Software: PyCharm
# @File    : reverse_vowels.py

import re


class Solution:
    def __init__(self):
        """
        """
        pass

    def isVowel(self, s):
        return s in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # if re.search(r'[aeiouAEIOU]', s):
        #     return True
        # return False

    def reverseVowels(self, s):
        li, start, end = list(s), 0, len(s) - 1
        while start < end:
            l = self.isVowel(li[start])
            r = self.isVowel(li[end])
            if l and r:
                li[start], li[end] = li[end], li[start]
                start += 1
                end -= 1
            elif l:
                end -= 1
            elif r:
                start += 1
            else:
                start += 1
                end -= 1
        return ''.join(li)


if __name__ == '__main__':
    s = Solution()
    ss = 'leetcode'
    print(s.reverseVowels(ss))
    print(ss)
