# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 16:42
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : integer_to_roman.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/integer-to-roman/
        罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
        '''
        pass

    def intToRoman(self, num: int) -> str:
        dic = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
               5: 'V', 4: 'IV', 1: 'I'}
        li1 = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        li2 = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        result = ''
        if num < 1 or num > 3999:
            return ''
        count = len(li1)
        for i in range(count):
            a = num // li1[i]
            num = num % li1[i]
            if a > 0:
                result += li2[i] * a
            if num == 0:
                break

        # for i in range(len(li1)):
        #     tmp, num = divmod(num, li1[i])
        #     result += li2[i] * tmp

        # for i in range(len(li1)):
        #     while li1[i] <= num:
        #         num -= li1[i]
        #         result += li2[i]
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(1987))
