# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 10:16
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : reverse_str.py
# @Software: PyCharm
import math


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/reverse-string-ii/
        给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。

示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"
要求:

该字符串只包含小写的英文字母。
给定字符串的长度和 k 在[1, 10000]范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-string-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        '''
        pass

    def reverseStr(self, s: str, k: int) -> str:
        length = len(s)
        if length < k:
            return s[::-1]
        if k == 1:
            return s
        res, start, end = '', 0, 2 * k
        while end <= length:
            res += s[start:start + k][::-1]
            res += s[start + k:start + 2 * k]
            start += 2 * k
            end += 2 * k
        if length - start > k:
            res += s[start:start + k][::-1]
            res += s[start + k:]
        else:
            res += s[start:][::-1]
        return res

    def reverseStr2(self, s: str, k: int) -> str:
        length = len(s)
        sl = [s[i:i + k] for i in range(0, length, k)]
        sl = [sl[i][::-1] if i % 2 == 0 else sl[i] for i in range(len(sl))]
        return ''.join(sl)
        # res = ''
        # for i in range(len(sl)):
        #     if i % 2 == 0:
        #         res += sl[i][::-1]
        #     else:
        #         res += sl[i]
        # return res






if __name__ == '__main__':
    s = Solution()
    res = s.reverseStr('abcdefgh', 3)
    res2 = s.reverseStr2('abcdefgh', 3)
    print(res, res2)
