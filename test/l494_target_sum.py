#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2020/6/30 9:20
# @Software: PyCharm
# @File    : l494_target_sum.py

class Solution:
    def __init__(self):
        '''

        '''
        pass

    def findTargetSumWays(self, nums, S) -> int:
        total = sum(nums)
        target = (total + S) // 2
        if len(nums) == 1:
            return 1 if nums[0] == S or nums[0] == -S else 0
        if total < S or (total + S) % 2 == 1:
            return 0
        zeros = [0 for i in nums if i == 0]
        res = 1
        if len(zeros) > 0:  # 处理0的边界问题 每个元素有用和不用两种可能 所以是2的N次方
            res *= 2 ** len(zeros)
        nums = [i for i in nums if i != 0]
        tmp = self.subsets(nums, target)
        if tmp > 0:
            res *= tmp
        return res

    def subsets(self, nums, target):
        '''
        dp[i][j]  标识前i个元素target=j时，最大的组合数
        :param nums:
        :param target:
        :return:
        '''
        total = max(target, len(nums)) + 1
        dp = [[0 for i in range(total)] for j in range(len(nums) + 1)]
        n = len(nums)
        # print(dp)
        for i in range(n):
            dp[i][0] = 1
        # print(dp, nums)
        for i in range(1, n + 1):
            for j in range(1, total):
                t1 = dp[i - 1][j]  # 不用当前元素
                t2 = 0 if j - nums[i - 1] < 0 else dp[i - 1][j - nums[i - 1]]  # 用当前元素
                dp[i][j] = t1 + t2
                # print(t1, t2, j, nums[i])
        # print(dp)
        return dp[n][target]


if __name__ == '__main__':
    s = Solution()
    nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    target = 0
    res = s.findTargetSumWays(nums, target)
    print(res)
