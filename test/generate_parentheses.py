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

    @lru_cache(None)
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

    def generateParenthesis3(self, n):
        if n == 0: return ['']
        ans = []
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n - 1 - i):
                    ans.append('({}){}'.format(left, right))
        return ans

    def generateParenthesis4(self, n):
        res = []

        def recur(left, right, s):
            # 终止条件
            if left == n and right == n:
                # print(s)
                res.append(s)
                return
            # 当前逻辑

            # 往下递归
            if left < n:
                recur(left + 1, right, s + "(")
            if right < left:
                recur(left, right + 1, s + ')')

            # 状态处理
            # pass

        recur(0, 0, '')
        return res

    def generateParenthesis5(self, n):
        def generate(p, left, right, parens=[]):
            if left:
                generate(p + '(', left - 1, right)
            if right > left:
                generate(p + ')', left, right - 1)
            if not right: parens += p,
            return parens

        return generate('', n, n)


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis5(3))
    # print(s.generateParenthesis1(3))
    # print(s.generateParenthesis(3))
    # print(len(s.generateParenthesis1(4)))

    # pass
