#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2020/5/11 10:51
# @Software: PyCharm
# @File    : l312burst_ballons.py

class Solution:
    def __init__(self):
        """
        有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
求所能获得硬币的最大数量。

        说明:
        你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
        0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
        示例:
        输入: [3,1,5,8]
        输出: 167
        解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
        """
        pass

    def maxCoins(self, nums) -> int:
        n, points = len(nums), nums
        points.append(1)
        points.insert(0, 1)
        dp = [[0 for i in range(n + 2)] for j in range(n + 2)]
        for i in range(n, -1, -1):
            for j in range(i + 1, n + 2):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + points[i] * points[j] * points[k])
        return dp[0][n + 1]


if __name__ == '__main__':
    s = Solution()
    nums = [3, 1, 5, 8]
    print(s.maxCoins(nums))
