# -*- coding: utf-8 -*-
# @Time    : 2019/4/12 17:35
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : multiply_strings.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/multiply-strings/
        给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

        示例 1:

        输入: num1 = "2", num2 = "3"
        输出: "6"
        示例 2:

        输入: num1 = "123", num2 = "456"
        输出: "56088"
        说明：

        num1 和 num2 的长度小于110。
        num1 和 num2 只包含数字 0-9。
        num1 和 num2 均不以零开头，除非是数字 0 本身。
        不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
        '''

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        m, n = len(num1), len(num2)
        li = [0] * (m + n + 1)
        zero = 0
        for i in range(len(num1) - 1, -1, -1):
            if num1[i] == '0':
                zero += 1
            else:
                break
        for i in range(len(num2) - 1, -1, -1):
            if num2[i] == '0':
                zero += 1
            else:
                break
        for i in range(m):
            for j in range(n):
                t_1, t_2 = int(num1[i]), int(num2[j])
                if t_1 == 0:
                    break
                if t_2 == 0:
                    continue
                li[i + j] += t_1 * t_2
        count, res = 0, 0
        while True:
            s = li.pop()
            if s != 0:
                break
        li.append(s)
        li.reverse()
        for i in li:
            res += i * (10 ** count)
            count += 1
        return str(int(res * (10 ** zero)))


if __name__ == '__main__':
    s = Solution()
    print(s.multiply('22', '554'))
    print(22 * 554)
