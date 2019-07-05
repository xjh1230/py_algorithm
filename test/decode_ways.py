# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 10:33
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : decode_ways.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/decode-ways/
        一条包含字母 A-Z 的消息通过以下方式进行了编码：
        'A' -> 1
        'B' -> 2
        ...
        'Z' -> 26
        给定一个只包含数字的非空字符串，请计算解码方法的总数。
        示例 1:
        输入: "12"
        输出: 2
        解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
        '''

    def numDecodings(self, s: str) -> int:
        if len(s) < 1 or s[0] == '0':
            return 0
        res = [0] * len(s)
        res[0] = 1
        for i in range(1, len(s)):
            tmp = int(s[i - 1:i + 1])
            prev = tmp // 10
            cur = tmp % 10
            if cur == 0:
                if prev > 2 or prev == 0:
                    return 0
                else:
                    res[i] = res[i - 1]
            else:
                if tmp > 26:
                    res[i] = res[i - 1]
                elif prev == 0:
                    res[i] = res[i - 1]
                else:
                    res[i] = res[i - 1] + (res[i - 2] or 1)
        print(res)
        if s[-1] == '0':
            res[-1] = res[-3] if len(s) > 2 else res[-2]
        return res[-1]


if __name__ == '__main__':
    sl = Solution()
    s = '12210'
    c = sl.numDecodings(s)
    print(c)
