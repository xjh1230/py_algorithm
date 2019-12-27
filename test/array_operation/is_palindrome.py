#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/12/26 16:45
# @Software: PyCharm
# @File    : is_palindrome.py

import re


class Solution:
    def __init__(self):
        """
        """
        pass

    def isPalindrome(self, s):
        s = re.sub('[^\da-zA-Z]', '', s)
        s = s.lower()
        s = s.replace(' ', '')
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

    def isPalindrome1(self, s):
        s = s.lower()
        start, end = 0, len(s) - 1
        while start < end:
            if not s[start].isalunm():
                start += 1
            if not s[end].isalunm():
                end -= 1
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True
