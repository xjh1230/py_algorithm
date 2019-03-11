# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 14:29
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : generate_parentheses.py
# @Software: PyCharm

from functools import lru_cache


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/generate-parentheses/
        给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
        '''
        pass

    def generateParenthesis1(self, n):
        def backtrack(S='', left=0, right=0):

            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)

        ans = []
        backtrack()
        return ans

    def generateParenthesis(self, n):
        def generate(a=[]):
            if len(a) == 2 * n:
                print(a)
                if valid(a):
                    ans.append(''.join(a))
            else:
                a.append('(')
                generate(a)
                a.pop()
                a.append(')')
                generate(a)
                a.pop()

        def valid(a):
            b = 0
            for i in a:
                if i == '(':
                    b += 1
                else:
                    b -= 1
                if b < 0:
                    return False
            return b == 0

        ans = []
        generate()
        return ans

    def generateParenthesis2(self, n):
        result = []
        if n < 1:
            return result
        for i in range(1, n + 1):
            tmp = '(' * i + ')'
            count_l = i
            count_r = 1
            while len(tmp) < 2 * n:
                if count_l == n:
                    tmp += ')' * (2 * n - len(tmp))
                else:
                    for j in range(n - count_r):
                        tmp += ')' * j
            # print(tmp, i)
            result.append(tmp)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis2(3))
    print(s.generateParenthesis1(3))
    # print(len(s.generateParenthesis1(4)))
