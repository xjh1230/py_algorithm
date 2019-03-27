# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 9:45
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : z_convert.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        '''
        将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

        比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

        L   C   I   R
        E T O E S I I G
        E   D   H   N
        之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
        '''
        pass

    def convert1(self, s, num_rows):
        """
        :type s: str
        :type num_rows: int
        :rtype: str
        """
        result_tmp = []
        result = ''
        index = 0
        count = len(s) - 1
        column = 0
        if num_rows <= 1 or num_rows > count:
            return s
        for i in range(num_rows):
            result_tmp.append([])
        while index <= count:
            if column % (num_rows - 1) == 0:  # 每一行都添加
                for j in range(num_rows):
                    if index > count:
                        break
                    result_tmp[j].append(s[index])
                    index += 1
                    # print(result_tmp, column)
            else:  # 特定行添加
                for j in range(num_rows):
                    tmp = num_rows - 1 - column % (num_rows - 1)
                    if index > count:
                        # print(result_tmp, '普通', column, tmp, index, len(s))
                        break
                    if (tmp + j) % (num_rows - 1) == 0 and tmp > 0:
                        result_tmp[tmp].append(s[index])
                        index += 1
                        # print(result_tmp, '普通', column, tmp)
            column += 1
        for i in result_tmp:
            # print(i)
            result += ''.join(i)
        return result

    def convert(self, s, num_rows):
        '''
        找规律  num_rows = 4
        0     6     12
        1   5 7   11
        2 4   8 10
        3     9
        每一行的前一个元素和后一个元素间隔 （num_rows-1）*2 个元素
        被除数 c 为（num_rows-1）*2
        当前索引除以 c  余 n n>num_rows-1 则n=c-n 则将当前数字放在第n个list
        最后结果是list拼接
        :param s:
        :param num_rows:
        :return:
        '''
        result = ''
        index = 0
        count = len(s) - 1
        if num_rows <= 1 or num_rows > count:
            return s
        be_div = (num_rows - 1) * 2
        li_tmp = [i for i in range(num_rows)]
        result_tmp = [[] for i in range(num_rows)]
        for i in s:
            tmp = index % be_div
            if tmp >= num_rows:
                tmp = be_div - tmp
            # print(tmp, result_tmp, i)
            result_tmp[tmp].append(i)
            index += 1
        for i in result_tmp:
            result += ''.join(i)
        return result

    def test(self):
        s = 'LEETCODEISHIRING'
        num_rows = 4
        print(self.convert(s, num_rows), s)
        num_rows = 3
        print(self.convert(s, num_rows), s)
        s = 'A'
        num_rows = 1
        print(self.convert(s, num_rows), s)
        s = 'ABC'
        num_rows = 2
        print(self.convert(s, num_rows), s)


if __name__ == '__main__':
    s = Solution()
    s.test()
