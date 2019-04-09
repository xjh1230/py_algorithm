# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 14:48
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : count_and_say.py
# @Software: PyCharm

from functools import lru_cache


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/count-and-say/
        报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
        1.     1
        2.     11
        3.     21
        4.     1211
        5.     111221
        1 被读作  "one 1"  ("一个一") , 即 11。
        11 被读作 "two 1s" ("两个一"）, 即 21。
        21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

        给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

        注意：整数顺序将表示为一个字符串。
        '''

    def countAndSay1(self, n: int) -> str:
        lst = ['1', '11', '21']
        if n <= 3:
            return lst[n - 1]
        for i in range(3, n):
            before = str(lst[i - 1])
            base_num = 1
            base = ''
            for j in range(1, len(before)):
                if before[j] == before[j - 1]:
                    base_num += 1
                else:
                    base = base + str(base_num) + str(before[j - 1])
                    base_num = 1
            base = base + str(base_num) + str(before[j])
            lst.append(base)
        return lst[n - 1]

    @lru_cache(maxsize=33)
    def countAndSay(self, n: int) -> str:
        res = ['1', '11', '21']
        if n <= 3:
            return res[n - 1]
        before = self.countAndSay(n - 1)
        result = ''
        base_num = 1
        for i in range(1, len(before)):
            if before[i] == before[i - 1]:
                base_num += 1
            else:
                result += str(base_num) + str(before[i - 1])
                base_num = 1
        result += str(base_num) + str(before[i])
        return result

    def countAndSay2(self, n):
        if n == 1:
            return '1'
        s = '1'
        for _ in range(n - 1):
            res, before, count = '', s[0], 1
            for i in range(1, len(s)):
                if s[i] == before:
                    count += 1
                else:
                    res += str(count) + before
                    before = s[i]
                    count = 1
            res += str(count) + before
            s = res
        return s


if __name__ == '__main__':
    s = Solution()
    # s.countAndSay2(4)
    # print(s.countAndSay2(2))
    for i in range(1, 15):
        print(s.countAndSay2(i))
