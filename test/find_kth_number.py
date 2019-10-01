#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/9/17 17:46
# @Software: PyCharm
# @File    : find_kth_number.py


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def getCount(prefix, n):
            cur = prefix
            next = prefix + 1
            count = 0
            while cur <= n:
                count += min(n + 1, next) - cur
                cur *= 10
                next *= 10
            return count

        cur = 1
        res = 1
        while cur < k:
            count = getCount(res, n)
            if cur + count > k:
                res *= 10
                cur += 1
            elif cur + count <= k:
                res += 1
                cur += count
        return res

    def __init__(self):
        """
        """
        pass


if __name__ == '__main__':
    s = Solution()
    res = s.findKthNumber(10, 3)
    print(res)
