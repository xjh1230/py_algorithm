# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 16:38
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : roman_to_integer.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/roman-to-integer/
        '''
        pass

    def romanToInt(self, s: str) -> int:
        num = i = 0
        count = len(s)
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        while i < count:
            cur, next = dic[s[i]], dic[s[i + 1]] if i + 1 < count else 0
            dis = next / cur
            if (dis == 10 or dis == 5) and (cur != 5 or cur != 50):
                num += (next - cur)
                i += 2
            else:
                num += dic[s[i]]
                i += 1
        return num


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('III'))
