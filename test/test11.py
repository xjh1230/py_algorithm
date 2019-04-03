#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xm1230
# datetime:2019/3/3 0:19
# software: PyCharm

class Solution:
    def __init__(self):
        self.dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def longestPalindrome(self, s: str) -> str:
        i = l = r1 = r2 = maxc = 0
        count = len(s)
        dic = {}
        if count < 2:
            return s
        while i < count - 1:
            if s[i] == s[i + 1]:
                l = i
                r1 = i + 1
                tmp = ''
                while l > -1 and r1 < count:
                    if s[l] == s[r1]:
                        tmp = s[l] + tmp + s[r1]
                        l -= 1
                        r1 += 1
                    else:
                        break
                if len(tmp) > maxc:
                    maxc = len(tmp)
                    dic[maxc] = tmp
            l = i - 1
            r2 = i + 1
            tmp = s[i]
            while l > -1 and r2 < count:
                if s[l] == s[r2]:
                    tmp = s[l] + tmp + s[r2]
                    l -= 1
                    r2 += 1
                else:
                    break
            if len(tmp) > maxc:
                maxc = len(tmp)
                dic[maxc] = tmp
            i += 1
            if (count - i + 1) * 2 < maxc:
                break
        return dic[maxc]

    def romanToInt(self, s: str) -> int:
        num = i = 0
        count = len(s)
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        while i < count:
            cur, next = dic[s[i]], dic[s[i + 1]] if i + 1 < count else 0
            dis = next / cur
            if (dis == 10 or dis == 5) and (cur != 5 or cur != 50):
                num += (next - cur)
                i += 2
            else:
                num += dic[s[i]]
                i += 1
        return num


def reverse(str):
    start, end = 0, len(str) - 1
    str = list(str)
    while start < end:
        str[start], str[end] = str[end], str[start]
        start += 1
        end -= 1
    return ''.join(str)


print(reverse(''))

li = [[1, 3], [8, 10], [2, 6], [15, 18]]
li2 = sorted(li, key=lambda s: s[0])
print(li2)
if __name__ == '__main__':
    s = Solution()
    # print(s.longestPalindrome("ababababa"))
    print(s.romanToInt('III'))
    print(s.romanToInt('IV'))
    print(s.romanToInt('III'))
    print(s.romanToInt('LVIII'))
    print(s.romanToInt('MCMXCIV'))
