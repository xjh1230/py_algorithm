# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 12:54
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : reverse-integer.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/reverse-integer/
        给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

        示例 1:

        输入: 123
        输出: 321
        '''
        pass

    def reverse(self, x: int) -> int:
        result = 0
        sign = 1 if x > 0 else -1
        x = x * sign
        while x > 0:
            result = result * 10 + x % 10
            x = x // 10
        # if len(bin(result)) >= 34:
        #     result = 0
        # result = result * sign
        # return result

        result = result * sign
        if -2 ** 31 < result < 2 ** 31 - 1:
            return result
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(120))
    print(s.reverse(1534236469))
    print(s.reverse(-2147483412))
    print(s.reverse(1563847412))
