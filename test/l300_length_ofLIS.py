#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2020/1/2 15:43
# @Software: PyCharm
# @File    : l300_length_ofLIS.py

import bisect


class Solution:
    def __init__(self):
        """
        给定一个无序的整数数组，找到其中最长上升子序列的长度。
        示例:

        输入: [10,9,2,5,3,7,101,18]
        输出: 4
        解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
        说明:

        可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
        你算法的时间复杂度应该为 O(n2) 。
        进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
        """
        pass

    def lengthOfLIS1(self, nums) -> int:
        if len(nums) < 2:
            return len(nums)
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            tmp = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    tmp = max(tmp, dp[j])
            dp[i] = tmp + 1
        return max(dp)

    def lengthOfLIS(self, nums) -> int:
        # [1,7,2,4,5,3,4,5]
        if len(nums) < 2:
            return len(nums)
        res = []
        for n in nums:
            if not res or n > res[-1]:
                res.append(n)
            else:
                index = bisect.bisect_left(res, n)
                res[index] = n
        print(res)
        return len(res)


if __name__ == '__main__':
    s = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    nums = [1, 2, 3, 4, 5, 6, 7]
    nums = [1, 7, 8, 2, 3, 4, 5, 9, 10, 11, 12]
    nums = [1, 7, 2, 4, 5, 3, 6]
    res = s.lengthOfLIS(nums)
    print(res)
