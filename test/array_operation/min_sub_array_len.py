#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/12/26 17:26
# @Software: PyCharm
# @File    : min_sub_array_len.py

class Solution:
    def __init__(self):
        """
        1，2，3，4，5，6，7，8
        for 1 to 8:
            1+..6>=s
            2直接从6开始加 不用再遍历2...6
        """
        pass

    def minSubArrayLen(self, s, nums):
        if sum(nums) < s:
            return 0
        if max(nums) >= s:
            return 1
        tmp_sum, tmp, res, i = nums[0], 0, len(nums), 0
        while i < len(nums):
            total = tmp_sum
            for j in range(tmp + 1, len(nums)):
                total += nums[j]
                tmp = j
                if total >= s:
                    tmp_sum = total
                    while tmp_sum >= s:
                        tmp_sum -= nums[i]
                        if tmp_sum >= s:
                            i += 1
                        else:
                            break
                    res = min(res, j - i + 1)
                    break
            i += 1
        return res


if __name__ == '__main__':
    sc = Solution()
    s = 14
    nums = [2, 3, 1, 2, 4, 3]
    # nums = [1, 2, 3, 4, 5]
    res = sc.minSubArrayLen(s, nums)
    print(res)
