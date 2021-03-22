#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2021/3/22 13:46
# @Software: PyCharm
# @File    : l21_exchange.py

class Solution:
    def exchange_1(self, nums):
        odd, even = [], []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        while len(even) > 0 and len(odd) > 0 and even[0] < odd[-1]:
            e = even.pop(0)
            o = odd.pop()
            nums[e], nums[o] = nums[o], nums[e]
        return nums

    def exchange_2(self, nums):
        odd, even = [], []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        odd.extend(even)
        return odd

    def exchange(self, nums):
        start_e, len_e = -1, 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:  # 偶数
                if start_e == -1:
                    start_e = i
                len_e += 1
            else:  # 奇数
                if len_e > 0:  # 前面有偶数
                    nums[i], nums[start_e] = nums[start_e], nums[i]
                    start_e += 1
        return nums


if __name__ == '__main__':
    s = Solution()
    # li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17]
    li = [2, 4, 6]
    li = [1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 14, 16, 19]
    print(s.exchange(li))
