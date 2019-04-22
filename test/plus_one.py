# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 17:09
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : plus_one.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/plus-one/
        给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
        最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
        你可以假设除了整数 0 之外，这个整数不会以零开头。
        示例 1:
        输入: [1,2,3]
        输出: [1,2,4]
        解释: 输入数组表示数字 123。
        '''

    def plusOne(self, digits):
        li = [str(i) for i in digits]
        num = int(''.join(li)) + 1
        res = [int(i) for i in str(num)]
        return res

    def plusOne1(self, digits):
        from functools import reduce
        num = int(reduce(lambda x, y: str(x) + str(y), digits)) + 1
        res = [int(i) for i in str(num)]
        return res


    def plusOne3(self, digits):
        res, add = [], 1
        for i in digits[::-1]:
            res.append((i + add) % 10)
            add = (i + add) // 10
        if add == 1:
            res.append(1)
        return res[::-1]


if __name__ == '__main__':
    s = Solution()
    li = [1, 2, 3]
    li2 = s.plusOne3(li)
    print(li2)
