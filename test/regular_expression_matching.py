#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xm1230
# datetime:2019/3/9 20:16
# software: PyCharm

class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/regular-expression-matching/
给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。
匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
        '''
        pass

    def isMatch(self, s, p):
        s_len, p_len = len(s), len(p)
        if p_len > 0 and p[0] == '*':
            return False
        dp = [[False for i in range(p_len + 1)] for i in range(s_len + 1)]  # 创建结果集合  [s][p]
        dp[0][0] = True
        # 初始化,当s为空时候 p应为a*模式
        for i in range(1, len(dp[0])):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]  # a*c *是否配置 取决于a前面即dp[0][0] 默认True
        for i in range(1, s_len + 1):  # 遍历每个s
            for j in range(1, p_len + 1):  # 遍历每个p  s的每个字符是否匹配p的每个字符
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':  # 匹配模式，当前是否匹配，取决于前一次是否匹配
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':  # a*模式
                    if (s[i - 1] == p[j - 2]) or p[j - 2] == '.':  # a*或.* 匹配上a
                        dp[i][j] = dp[i][j - 1] or dp[i][j - 2] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 2]  # 当前ba*是否匹配取决于b是否匹配
                else:  # 不匹配 默认为False
                    pass
        for i in dp:
            print(i)
        return dp[s_len][p_len]


def isMatch2(self, s, p):
    '''
    递归实现
    :param s:
    :param p:
    :return:
    '''
    m, n = len(s), len(p)
    if n == 0:  # 正则为空，待匹配必须为空
        return m == 0
    if m == 0:  # 待匹配为空，验证正在是不是 'a*'模式
        if n >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:])
        else:
            return False
    # 匹配模式
    # 第一个字符是否相同
    firstMatch = s[0] == p[0] or p[0] == '.'
    if n >= 2 and p[1] == '*':  # 正则是'a*'模式，则选择 s[0] 或者去除s[0]
        return self.isMatch(s, p[2:]) or (firstMatch and self.isMatch(s[1:], p))
    else:  # 匹配模式
        return firstMatch and self.isMatch(s[1:], p[1:])


def isMatch1(self, s: str, p: str) -> bool:
    if p == '.*':
        return True
    count_p, count_s, i, j = len(p), len(s), 0, 0
    while i < count_p:
        if j >= count_s:  # s已经结束，p还未结束
            while i < count_p:
                if i + 1 < count_p and p[i + 1] == '*':  # 判断p最后是否全是 '.*
                    i += 2
                else:
                    return False
            return True
        if i + 1 == count_p:  # 最后一个元素
            if s[j] != p[i] and p[i] != '.':
                return False
            else:
                return j + 1 == count_s
        elif p[i + 1] == '*':
            if p[i] == '.':
                if i + 2 == count_p:
                    return True
                else:
                    while j < count_s:
                        if s[j] == p[i + 2]:
                            break
                        else:
                            j += 1
                    i += 2
            else:
                while j < count_s:
                    if s[j] == p[i]:
                        j += 1
                    else:
                        break
                i += 2
                if p[i] == p[i - 2]:  # 'aaa  a*a格式'
                    j -= 1
        else:
            if p[i] == '.' or p[i] == s[j]:
                i += 1
                j += 1
            else:
                return False
    return j == count_s


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch('aa', 'a*'))
    # print(s.isMatch('ab', '.*'))
    # print(s.isMatch('aa', 'a'))
    # print(s.isMatch('aab', 'c*a*b'))
    # print(s.isMatch('mississippi', 'mis*is*p*'))
    # print(s.isMatch('aa', 'a*'))
