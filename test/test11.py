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

    def superEggDrop(self, k, n):
        '''
        若干层楼，若干个鸡蛋，让你算出最少的尝试次数，找到鸡蛋恰好摔不碎的那层楼。国内大厂以及谷歌脸书面试都经常考察这道题，只不过他们觉得扔鸡蛋太浪费，改成扔杯子，扔破碗什么的。
        '''
        memo = dict()
        self.count = 0

        def dp(k, n):
            if k == 1: return n
            if n == 0: return 0
            if (k, n) in memo:
                return memo[(k, n)]
            res = float('INF')
            for i in range(1, n + 1):
                self.count += 1
                res = min(res, max(dp(k, n - i)  # 没碎
                                   , dp(k - 1, i - 1)  # 碎了
                                   ) + 1)
            memo[(k, n)] = res
            return res

        res = dp(k, n)
        print(self.count)
        return res

    def superEggDrop2(self, k, n):
        memo = dict()
        self.count = 0

        def dp(k, n):
            if k == 1: return n
            if n == 0: return 0
            if (k, n) in memo:
                return memo[(k, n)]
            res = float('INF')
            # for i in range(1, n + 1):
            #     self.count += 1
            #     res = min(res, max(dp(k, n - i)  # 没碎
            #                        , dp(k - 1, i - 1)  # 碎了
            #                        ) + 1)
            #  dp(k,n-i)  随i单调递减 A
            #  dp(k-1,i-i) 随i单调递增 B
            #  找到A与B的交叉点 取A的前半段B的后半段取最小值
            # memo[(k, n)] = res
            lo, hi = 1, n
            while lo <= hi:
                self.count += 1
                mid = lo + (hi - lo) // 2
                broken = dp(k - 1, mid - 1)
                no_broken = dp(k, n - mid)
                if broken > no_broken:
                    res = min(res, broken + 1)
                    hi = mid - 1
                else:
                    res = min(res, no_broken + 1)
                    lo = mid + 1
            memo[(k, n)] = res
            return res

        res = dp(k, n)
        print(self.count)
        return res

    def search(self, li, target):
        left, right = 0, len(li)
        while left < right:
            mid = left + (right - left) // 2
            if li[mid] == target:
                return mid
            elif li[mid] < target:
                left += 1
            else:
                right -= 1
        return -1


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
    # li = [1, 2, 3, 5, 6, 7, 8, 9]
    # print(s.search(li, 1))
    # print(s.longestPalindrome("cdababababadd"))
    print(s.superEggDrop(2, 10))
    print(s.superEggDrop2(2, 10))
    # print(s.romanToInt('III'))
    # print(s.romanToInt('IV'))
    # print(s.romanToInt('III'))
    # print(s.romanToInt('LVIII'))
    # print(s.romanToInt('MCMXCIV'))
