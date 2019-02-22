# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 12:00
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : kuo_hao_valid.py
# @Software: PyCharm

class Solution:
    def isValid(self, str):
        li_tmp = []
        count = len(str)
        if count % 2 == 1:
            return False
        li = [i for i in range(len(str)) if i % 2 == 0]
        i = 0
        while i < len(str):
            if len(li_tmp) > 0:
                s1 = li_tmp.pop()
                if not self.valid(s1, str[i]):
                    li_tmp.append(s1)
                    li_tmp.append(str[i])
                i += 1
            else:
                if not self.valid(str[i], str[i + 1]):
                    li_tmp.append(str[i])
                    li_tmp.append(str[i + 1])
                i += 2
        return len(li_tmp) == 0

    def valid(self, str1, str2):
        if str1 == '(':
            return str2 == ")"
        elif str1 == '[':
            return str2 == ']'
        elif str1 == '{':
            return str2 == '}'
        else:
            return False


if __name__ == '__main__':
    c = Solution()
    print(c.isValid('(){}[]'))
    print(c.isValid('({[]})'))
    print(c.isValid('({}[])'))
    print(c.isValid('(({[]}[]){})'))
    print(c.isValid('({[}])'))
