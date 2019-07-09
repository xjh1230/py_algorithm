# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 14:29
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : string_to_integer_atoi.py
# @Software: PyCharm

import re


class Solution:
    def __init__(self):
        '''
        请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：

假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，qing返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

示例 1:

输入: "42"
输出: 42
        '''
        pass

    def myAtoi1(self, str: str) -> int:
        s = re.sub(r'^\s*', '', str)
        if (s.startswith('+-')):
            return 0
        s = re.sub(r'^\+?', '', s)
        match_obj = re.match(r'^(-)?[\d]+', s)
        result = 0
        if match_obj:
            result = int(match_obj.group())
        return self.check_num(result)

    def myAtoi(self, str: str) -> int:
        start, result, symb, tmp = 0, 0, 1, '0'
        for s in str:
            if s == ' ':
                pass
            else:
                if s == '+' or s == '-':
                    start += 1
                    if s == '-':
                        symb = -1
                    break
                elif self.is_num(s):
                    break
                else:
                    return result
            start += 1
        end = start
        while end < len(str):
            if not self.is_num(str[end]):
                break
            end += 1
        result = int(tmp + str[start:end]) * symb
        return self.check_num(result)

    def is_num(self, s):
        return re.match('[\d]+', s)

    def check_num(self, num):
        int_max = (1 << 31) - 1
        int_min = (1 << 31) * -1
        if num > int_max:
            num = int_max
        elif num < int_min:
            num = int_min
        return num


def maxCount(m: int, n: int, ops) -> int:
    li_left = [m]
    li_right = [n]
    if ops and len(ops[0]) > 0:
        for li in ops:
            li_left.append(li[0])
            li_right.append(li[1])
    return min(li_left) * min(li_right)


if __name__ == '__main__':
    s = Solution()
    str = 'asd123'
    print(s.myAtoi(str))
